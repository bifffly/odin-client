import socket

history = []

while True:
    req = input("> ").strip()

    if req.lower() == "q":
        break
    if req.lower() == "b":
        if len(history) >= 2:
            history.pop()
            req = history.pop()
        else:
            print("No more history")
            continue

    try:
        while True:
            s = socket.create_connection(("127.0.0.1", "1866"))
            s.sendall(req.encode("UTF-8"))

            fp = s.makefile("rb")
            header = fp.readline()
            header = header.decode("UTF-8").strip()
            version, status = header.split()
            if status == "B":
                print("Error code B: file not found")
                break
            elif status != "A":
                print("Error code", status)
                break
            else:
                break
            break
    except Exception as err:
        print(err)
        continue

    if version == "rydja1":
        body = fp.read()
        body = body.decode("UTF-8")
        print(body)

    history.append(req)
