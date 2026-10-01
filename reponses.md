# Exercice n°1 :

Question n°1 :
Le verbe c'est POST, le code c'est 201

Question n°2 :
Il faut renvoyer 404 Not Found

Question n°3 :
401 = Unauthorized
403 = Forbidden

401 le serveur ne sait pas qui on est. Donc il faut s'authentifier
403 le serveur sait qui on est, mais refuse la connexion

# Exercice n°3 :

Terminal 1 :

```bash

  kiri   ~/Documents/cours/Python Backend & FastAPI/Eval   main ✚1 ↑9   12:05 
❯  source "/home/kiri/Documents/cours/Python Backend & FastAPI/Eval/.venv/bin/activate"

  kiri   ~/Documents/cours/Python Backend & FastAPI/Eval   main ✚1 ↑9   12:05 
❯ curl -s -X POST http://127.0.0.1:8000/stations -H "Content-Type: application/json" -d '{"code": "P1", "name": "Persistance", "capacity": 12}'
{"code":"P1","name":"Persistance","capacity":12,"status":"open","id":1}
  kiri   ~/Documents/cours/Python Backend & FastAPI/Eval   main ✚1 ↑9   12:05 
❯ curl -s http://127.0.0.1:8000/stations
[{"code":"P1","name":"Persistance","capacity":12,"status":"open","id":1}]
  kiri   ~/Documents/cours/Python Backend & FastAPI/Eval   main ✚1 ↑9   28.1s   12:06 
❯
```

Terminal 2 :

```bash
  kiri   ~/Documents/cours/Python Backend & FastAPI/Eval   main ↑9   3m20s   12:04 
❯ uvicorn app.main:app
INFO:     Started server process [193076]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     127.0.0.1:40818 - "POST /stations HTTP/1.1" 201 Created
^CINFO:     Shutting down
INFO:     Waiting for application shutdown.
INFO:     Application shutdown complete.
INFO:     Finished server process [193076]

  kiri   ~/Documents/cours/Python Backend & FastAPI/Eval   main ✚1 ↑9   1m13s   12:06 
❯ uvicorn app.main:app
INFO:     Started server process [193710]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     127.0.0.1:60284 - "GET /stations HTTP/1.1" 200 OK
^CINFO:     Shutting down
INFO:     Waiting for application shutdown.
INFO:     Application shutdown complete.
INFO:     Finished server process [193710]

  kiri   ~/Documents/cours/Python Backend & FastAPI/Eval   main ✚1 ↑9   53.4s   12:06 
❯
```

Conclusion : ça marche bien
