# Proyecto Final
##### Nombre del Blog: Ultrablog
##### Integrantes: Matias Vera - Mariano De Leon
##### Comision: 34640
### Descripcion

 Proyecto simulando un Blog, el cual fue subdividio en 3 App:
- Blog: en la misma se trabajo todo lo referido a los post (CRUD), se encuentra el inicio y el about.
- Chat: en la misma se trabajo el sistema de mensajeria entre usuarios. 
- Usuario: en la misma se trabajo todo el sistema de Register, Login y Logout de los usuarios, como asi tambien su perfil y avatares.

### Funcionamiento

Para ingresar al inicio se debe ingresar a   [localhost/].
En la navbar encontramos 5 botones los cuales se detallan a continuacion: 
| Boton | URL | Descripcion |
| ------ | ------ | ------ |
| UltraBlog | localhost/| Nos lleva a la pagina de inicio.
| Inicio | localhost/| Nos lleva a la pagina de inicio.
| Sobre Nosotros | localhos/Blog/about | Nos lleva la informacion sobre nosotros.
| Ingresar | localhost/Usuario/ingreso | Nos permite loguearnos a través de usuario y contraseña.
| Registrarse | localhost/Usuario/registro | Nos permite registrarnos.

En la cuerpo de la pagina del lado izquierdo, encontramos los post creados ordenados por fecha, los cuales se detallan a continuacion: 
| Boton | URL | Descripcion |
| ------ | ------ | ------ |
| Titulo Post | localhost/Blog/post/</id>| Nos carga el post seleccionado.
| Leer mas | localhost/Blog/post/</id>| Nos carga el post seleccionado.
| Nombre autor | localhos/Usuario/perfil/</id> | Nos lleva al perfil del autor.

En el lado derecho del cuerpo de incio, encontramos el area de buscar,los post recientes y las categorias, los cuales se detallan a continuacion:
#### Buscar
| Boton | URL | Descripcion |
| ------ | ------ | ------ |
| Input(titulo del post) | --- | Debemos ingresar el titulo del post a buscar.
| Buscar | --- | Nos muestra todos los post, que contienen la palabra buscada.
#### Ultimos Post
| Boton | URL | Descripcion |
| ------ | ------ | ------ |
| Titulo Post | localhost/Blog/post/</id>| Nos carga el post seleccionado.
| Nombre autor | localhos/Usuario/perfil/</id> | Nos lleva al perfil del autor.
#### Categorias
| Boton | URL | Descripcion |
| ------ | ------ | ------ |
| Nombre Categoria | ---| Carga todos los post de la categoria seleccionada.

### Distribucion de Tareas
| App | Encargado | 
| ------ | ------ |
| Blog | Matias Vera|
| Chat | Matias Vera|
| Usuario | Mariano De Leon|
