# Dependabot: Security- und Versions-Updates konfigurieren

- STATUS: OPEN
- PRIORITY: 30
- TAGS: build,dependabot

## Ausgangslage (Stand 2026-11-14)

Das Repository hatte **113 offene Dependabot-Alerts** (8 critical, 53 high,
46 medium, 6 low), alle in `uv.lock` und alle in transitiven Abhängigkeiten.
Sie wurden manuell durch ein vollständiges `uv lock --upgrade` behoben
(siehe PR #106). Ohne Automatisierung sammelt sich das nächste Runde wieder an.

Aktuelle Repo-Einstellungen:

| Einstellung | Zustand |
|---|---|
| Dependabot alerts (Vulnerability alerts) | **aktiv** |
| Dependabot security updates | **aus** (`automated-security-fixes: enabled=false`) |
| `.github/dependabot.yml` | **existiert nicht** |
| Offene Dependabot-PRs | 0 |

Deshalb gab es Alerts, aber nie einen PR.

## Zu entscheiden

1. **Security updates aktivieren?** Das ist ein Repo-Toggle, *nicht* Teil von
   `dependabot.yml`. Er öffnet PRs auf die minimal gepatchte Version, sobald
   eine Advisory erscheint, ignoriert `schedule` und `cooldown` und ist auf
   10 offene PRs begrenzt. Ohne ihn gibt es nur dann einen Fix, wenn das
   nächste wöchentliche Versions-Update zufällig die Lücke schließt.
2. **Versions-Updates per `dependabot.yml`?** `package-ecosystem: uv` ist
   unterstützt (Lockfile-Schema `version = 1`). Standard sind ein PR pro
   Abhängigkeit und max. 5 offene PRs.
3. **Gruppieren oder nicht?** Mehrere Einzel-PRs ändern alle `uv.lock` und
   kollidieren nach dem ersten Merge. `groups: { python-deps: { patterns: ["*"] } }`
   bündelt alles in einen PR — dafür ist der PR groß und schwer zu reviewen.
4. **GitHub Actions mitpflegen?** `package-ecosystem: github-actions` hebt
   Action-Refs an. Für SHA-Pins (`astral-sh/setup-uv@cec2083… # v8.0.0`) wird
   nur dann aktualisiert, wenn der Tag als Kommentar **in derselben Zeile**
   steht. Hinweis: Für SHA-gepinnte Actions erzeugt Dependabot *keine* Alerts.
5. **Cooldown?** Seit 2025 gilt standardmäßig 3 Tage Karenz für
   Versions-Updates (nicht für Security-Updates). Für einen Kurs, der auf
   reproduzierbare Notebook-Ausgaben angewiesen ist, ggf. deutlich länger.

## Vorschlag zum Weiterdenken

```yaml
version: 2
updates:
  - package-ecosystem: uv
    directory: /
    schedule: { interval: weekly }
    groups:
      python-deps:
        patterns: ["*"]
    cooldown:
      default-days: 7
  - package-ecosystem: github-actions
    directory: /
    schedule: { interval: weekly }
```

Wichtig: `build.yml` läuft auf `pull_request` und führt
`jupyter book build --execute --all` aus. Jeder Dependabot-PR wird also
automatisch gegen den echten Build geprüft — das ist das eigentliche
Sicherheitsnetz für Major-Bumps (pandas, numpy, pillow).

## Offene Fragen

- Ist ein großer Sammel-PR oder sind thematisch getrennte Gruppen
  (z. B. `jupyter-*`, `pandas/numpy`, `pillow`) praktischer?
- Sollen Major-Updates grundsätzlich ignoriert werden
  (`ignore: update-types: [version-update:semver-major]`), weil sie im
  Kursinhalt sichtbare Änderungen erzeugen können?
- Wer reviewt die PRs, wenn sie automatisch eintreffen?

## Checkliste

- [ ] Entscheidung zu Security-Updates (Toggle) getroffen
- [ ] Entscheidung zu `dependabot.yml` und Gruppierung getroffen
- [ ] Config angelegt und ein Probelauf abgewartet
- [ ] Geprüft, ob Dependabot-PRs den Build-Check erfolgreich durchlaufen
- [ ] Umgang mit Major-Updates dokumentiert (ignore-Regel oder Review-Pflicht)
