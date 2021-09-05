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
            _, status = header.split()
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

    body = fp.read()
    body = body.decode("UTF-8")
    blist, nlist = False, False
    nlistnum = 1
    for line in body.splitlines():
        if line.startswith("@rydja"):
            print(line.split("(")[1].split(")")[0])
            print("----------")
        elif line.startswith("@head"):
            print("#", line.split("(")[1].split(")")[0])
        elif line.startswith("@hhead"):
            print("##", line.split("(")[1].split(")")[0])
        elif line.startswith("@hhhead"):
            print("###", line.split("(")[1].split(")")[0])
        elif line.startswith("@blist"):
            blist = not blist
        elif line.startswith("@nlist"):
            nlist = not nlist
            if not nlist:
                nlistnum = 1
        else:
            if blist:
                print("*", line)
            elif nlist:
                print(str(nlistnum) + ".", line)
            else:
                print(line)

    history.append(req)
