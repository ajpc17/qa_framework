# QA Framework - Automatización de Pruebas

Framework de testing automatizado construido con Python, Selenium y pytest.

## 🛠️ Tecnologías
- Python 3.12
- Selenium 4
- pytest
- GitHub Actions (CI/CD)

## 📁 Estructura

qa_framework/
├── config/          # Configuración global
├── pages/           # Page Object Model
├── tests/           # Tests automatizados
├── utils/           # Driver centralizado
├── reports/         # Screenshots y reportes HTML
└── conftest.py      # Fixtures compartidos

## ⚙️ Instalación
```bash
pip install selenium pytest pytest-html
```

## 🚀 Ejecutar tests
```bash
# Todos los tests
python -m pytest tests/ -v

# Con reporte HTML
python -m pytest tests/ -v --html=reports/report.html

# Un archivo específico
python -m pytest tests/test_login.py -v
```

## 🧪 Tests incluidos
| Archivo | Tests | Descripción |
|---------|-------|-------------|
| test_google.py | 2 | Búsqueda en Google |
| test_login.py | 3 | Login exitoso y fallido |
| test_checkboxes_dropdown.py | 4 | Formularios |
| test_alerts.py | 4 | Alertas del navegador |
| test_saucedemo.py | 7 | Tienda completa con Data Driven Testing |

## ✅ CI/CD
Cada push a main ejecuta todos los tests automáticamente en GitHub Actions.

## 👤 Autor
ajpc17