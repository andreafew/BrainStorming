#!/usr/bin/env python3
"""Importa backlog_unificado_completo.csv a GitHub (labels, milestones, issues, sub-issues).
Uso (desde la carpeta del repo):
  python backlog/importar.py --repo USUARIO/REPO [--project N --owner USUARIO] [--dry-run]
Se puede cortar y volver a correr: saltea los issues que ya existen."""
import argparse, csv, subprocess, sys, json, time, re
p = argparse.ArgumentParser()
p.add_argument("--repo", required=True); p.add_argument("--csv", default="backlog/backlog_unificado_completo.csv")
p.add_argument("--project", type=int); p.add_argument("--owner"); p.add_argument("--dry-run", action="store_true")
a = p.parse_args()

def gh(*args, check=True):
    if a.dry_run: print("gh", *args[:5], "..."); return ""
    for i in range(6):
        r = subprocess.run(["gh", *args], capture_output=True, text=True, encoding="utf-8")
        if r.returncode == 0: return r.stdout.strip()
        e = r.stderr.lower()
        if "rate limit" in e or "secondary" in e or "abuse" in e:
            print(f"GitHub pidió esperar; reintento en {30*(i+1)}s..."); time.sleep(30*(i+1)); continue
        break
    if check: print("ERROR:", r.stderr); sys.exit(1)
    return ""

rows = list(csv.DictReader(open(a.csv, encoding="utf-8-sig")))
slug = {"A - Estudio": "cliente-A-estudio", "B - Universidad": "cliente-B-universidad", "Ambos": "cliente-ambos", "Equipo": "equipo"}
def labels(r): return [r["Tipo"].lower(), slug[r["Cliente"]], f"sprint-{r['Sprint']}", f"SP-{r['Story Points']}", f"prioridad-{r['Prioridad'].lower()}"]
for l in sorted({x for r in rows for x in labels(r)}): gh("label", "create", l, "--repo", a.repo, "--force")

names = {1: "Sprint 1 - Relevamiento", 2: "Sprint 2 - Instalación", 3: "Sprint 3 - Pruebas y control de versiones", 4: "Sprint 4 - Recomendación, CI/CD y cierre"}
fechas = {int(r["Sprint"]): r["Fecha límite"] for r in rows}
for s, n in names.items():
    gh("api", f"repos/{a.repo}/milestones", "-f", f"title={n}", "-f", f"due_on={fechas[s]}T23:59:59Z", check=False)

exist = {}
if not a.dry_run:
    out = gh("issue", "list", "--repo", a.repo, "--state", "all", "--limit", "1000", "--json", "title,number,url")
    exist = {i["title"]: i for i in json.loads(out or "[]")}

creados = {}  # Ref -> (número, url)
orden = sorted(rows, key=lambda r: int(r["N.º"]))  # mismo orden que el Excel: así GitHub numera los issues en ese orden
for r in orden:
    t = r["Título"]
    if t in exist:
        creados[r["N.º"]] = (exist[t]["number"], exist[t]["url"]); print("Ya existe:", t); continue
    hecho = "x" if r["Estado"] == "Done" else " "
    ev = r["Evidencia"]
    if ev:
        evid = f"### Evidencia\n[Abrir el archivo de evidencia](https://github.com/{a.repo}/blob/main/{ev})\n\n"
        dod = f"- [{hecho}] Evidencia cargada en el archivo indicado\n- [{hecho}] PR revisado por otro integrante\n"
    else:
        evid = ""
        dod = f"- [{hecho}] Todas las tareas asociadas terminadas\n"
    body = (f"{r['Tipo']} · {r['Cliente']} · Story Points: {r['Story Points']} · Prioridad: {r['Prioridad']} · Límite: {r['Fecha límite']}\n"
            + (f"**Parte de:** {r['Padre título']}\n" if r['Padre título'] else "") + f"**Criterio de evaluación:** {r['Criterio ref'] or '-'}\n\n"
            f"### Descripción\n{r['Descripción']}\n\n### Criterio de aceptación\n{r['Criterio de aceptación']}\n\n"
            + evid + f"### Definition of Done\n{dod}")
    args = ["issue", "create", "--repo", a.repo, "--title", t, "--body", body, "--milestone", names[int(r["Sprint"])]]
    for l in labels(r): args += ["--label", l]
    url = gh(*args)
    if url: creados[r["N.º"]] = (int(url.rstrip("/").split("/")[-1]), url)
    if not a.dry_run: time.sleep(3)
    if r["Estado"] == "Done" and url: gh("issue", "close", url)
    if a.project and a.owner and url: gh("project", "item-add", str(a.project), "--owner", a.owner, "--url", url, check=False)

# sub-issues (mejor esfuerzo: si falla, se avisa y se sigue)
if not a.dry_run:
    for r in rows:
        if r["Padre"] and r["Padre"] in creados and r["N.º"] in creados:
            hijo_id = gh("api", f"repos/{a.repo}/issues/{creados[r['N.º']][0]}", "--jq", ".id", check=False)
            if hijo_id:
                gh("api", "-X", "POST", f"repos/{a.repo}/issues/{creados[r['Padre']][0]}/sub_issues", "-F", f"sub_issue_id={hijo_id}", check=False)
                time.sleep(1)
print("Listo:", len(rows), "filas")
