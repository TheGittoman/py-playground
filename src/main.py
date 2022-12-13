import galai as gl
import sys


def sanitiseArguments(argsv):
    if len(argsv) > 2 or len(argsv) <= 1:
        return False
    return True


def main():
    if sanitiseArguments(sys.argv):
        print("loading the model-----")
        model = gl.load_model(name="standard", num_gpus=1)
        print("model loaded----------")
        print("starting generation---")
        output = model.generate(sys.argv[1], max_length=400)
        print("Result:\n", output)
    print("Exiting the program")


# if this script is ran directly run main
if __name__ == "__main__":
    main()
