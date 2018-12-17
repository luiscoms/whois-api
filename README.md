Who is - API
============

Tornado api to get account by `CPF` number 

Running tests
-------------

```bash
$ tox
```

Running application
-------------------

See [multi-databases-py](https://github.com/luiscoms/multi-databases-py)

### Endpoints

```bash
$ curl http://localhost:8080/status
```

```json
{
    "version": "1.0.0",
    "branch": "76ee5ad (HEAD, tag: 1.0.0, origin/tags/1.0.0, origin/master, origin/develop) :bookmark: Release version: 1.0.0 - Luis Fernando Gomes"
}
```

```bash
$ curl http://localhost:8080/health
```

```json
{
    "hostname": "951f92f6e379",
    "status": "success",
    "timestamp": 1545062619.7322128,
    "results": [
        {
            "checker": "mysql_connected",
            "output": "MySQL ok",
            "passed": true,
            "timestamp": 1545062619.7130396,
            "expires": 1545062646.7130396,
            "response_time": 0.000016
        }
    ],
    "version": "0.0.0",
    "branch": "Not found"
}
```

```bash
$ curl http://localhost:8080/whois/37999854840
```

```json
{
    "id": 1,
    "first_name": "John",
    "last_name": "Doe",
    "cpf": "37999854840",
    "creation": "2018-12-16 12:58:06",
    "update": "2018-12-16 12:58:06"
}
```