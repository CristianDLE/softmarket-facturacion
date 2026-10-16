# Guia de contribucion

## Ramas
- main: produccion (protegida, cada merge lleva tag vX.Y.Z)
- develop: integracion (protegida)
- feature/<ticket>-<descripcion>: desde develop, vida maxima 2-3 dias
- release/X.Y.0: desde develop, solo correcciones de QA
- hotfix/X.Y.Z: desde main, para incidentes criticos

## Commits (Conventional Commits)
tipo(alcance): descripcion en imperativo, minuscula, max. 72 caracteres
Tipos: feat, fix, docs, style, refactor, test, chore, perf, ci, build

## Pull Requests
- Pequenos (< 400 lineas), con plantilla completa y CI en verde
- Minimo 1 aprobacion (2 para main); el autor no aprueba su propio PR
