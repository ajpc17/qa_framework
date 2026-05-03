# Comandos del Framework QA

## Instalar dependencias
pip install selenium pytest pytest-html python-dotenv pytest-xdist

## Ejecutar tests
# Todos los tests
python -m pytest tests/ -v

# Un archivo específico
python -m pytest tests/test_login.py -v

# Con reporte HTML
python -m pytest tests/ -v --html=reports/report.html

# En paralelo (más rápido)
python -m pytest tests/test_saucedemo.py -v -n auto

## Guardar cambios en GitHub
git add .
git commit -m "descripcion de lo que cambiaste"
git push

## Ver estado de los archivos modificados
git status

## Ver historial de commits
git log --oneline

Para Farma Humana:

Inspeccionar elementos → copiar IDs
Copiar una Page Object existente → cambiar URL e IDs
Copiar un test existente → cambiar datos
Ejecutar pytest