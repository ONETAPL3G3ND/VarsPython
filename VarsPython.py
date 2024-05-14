class Info:
    def __init__(self):
        self.version = "1.0"

    def GetVersion(self):
        return self.version

if __name__ == "__main__":
    print(vars(Info))