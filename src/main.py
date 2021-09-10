import socket
import urllib.parse

history = []

while True:
    cmd = input("> ").strip()
    if cmd.lower() == "q":
        break
    if cmd.lower() == "h":
        for cmd in history:
            print(cmd)
        continue
    if cmd.lower() == "b":
        if len(history) >= 2:
            history.pop()
            cmd = history.pop()
        else:
            print("No more history")
            continue

    try:
        while True:
            url = urllib.parse.urlparse(cmd)
            s = socket.create_connection((url.netloc, 1866))
            req = "odin\tpull\t" + url.path
            s.sendall(req.encode("UTF-8"))

            fp = s.makefile("rb")
            header = fp.readline()
            header = header.decode("UTF-8").strip()
            _, status = header.split()
            if status != "A":
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
        if line.startswith("@odin"):
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

    history.append(cmd)
