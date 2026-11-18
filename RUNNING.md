# Uso local de la colección

Fork personal de [scrollmapper/bible_databases_deuterocanonical](https://github.com/scrollmapper/bible_databases_deuterocanonical), rama `master`. El contenido actual del original es una biblioteca de textos Markdown/JSON con utilidades Python. No es una aplicación con base de datos SQL que haya que compilar.

Abre [readme.md](readme.md) para el catálogo, `sources/` para los textos principales y `etc/` para las demás colecciones. Se conservan los avisos y las atribuciones de las fuentes. La rama histórica `2024` del original contiene la estructura anterior.

## Validar sin cambiar datos

```powershell
python tools/validate-local.py
```

Requiere Python 3 y Git. Analiza todos los JSON versionados y comprueba la sintaxis de los scripts Python sin ejecutarlos. Devuelve un código distinto de cero ante un error. No comprueba la exactitud del contenido ni genera nuevos catálogos.

## Utilidades de generación

Los scripts originales usan rutas relativas a su directorio de trabajo. Si necesitas regenerar datos, trabaja primero en una rama y revisa el diff:

```powershell
cd scripts
python create_source_json_from_md.py
python generate_book_list.py
```

Estos comandos sí escriben JSON y catálogos dentro de la colección. No son necesarios para leerla. No se ejecutaron masivamente durante la sincronización para evitar sustituir datos del original.

`origin` apunta al fork personal y `upstream` al original; el push a upstream está deshabilitado localmente. Conserva el README original en minúsculas para evitar duplicados en Windows.
