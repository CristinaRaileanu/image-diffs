import argparse
import subprocess
from jsondiff import diff

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("--image", type=str, required=True)
    parser.add_argument("--v1", type=str, required=True)
    parser.add_argument("--v2", type=str, required=True)

    args = parser.parse_args()

    command1 = "sudo syft packages docker:" + args.image + ":" + args.v1 + " -o json"
    command2 = "sudo syft packages docker:" + args.image + ":" + args.v2 + " -o json"

    info1 = subprocess.run(command1, stdout=subprocess.PIPE, shell=True)
    info2 = subprocess.run(command2, stdout=subprocess.PIPE, shell=True)

    info1 = info1.stdout.decode("utf-8")
    info2 = info2.stdout.decode("utf-8")

    f = open("differences.json", "w")
    f.write(diff(info1, info2))
    f.close()
