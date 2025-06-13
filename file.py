class FSNode:
    def __init__(self, label, is_folder):
        self.label = label
        self.is_folder = is_folder
        self.children = {} if is_folder else None
        self.parent = None


class SimpleFileSystem:
    def __init__(self):
        self.root = FSNode("/", True)
        self.active = self.root

    def make_folder(self, name):
        if name in self.active.children:
            print("Folder already exists.")
        else:
            folder = FSNode(name, True)
            folder.parent = self.active
            self.active.children[name] = folder

    def make_file(self, name):
        if name in self.active.children:
            print("File already exists.")
        else:
            file = FSNode(name, False)
            file.parent = self.active
            self.active.children[name] = file

    def list_items(self):
        for item in sorted(self.active.children):
            print(item + ('/' if self.active.children[item].is_folder else ''))

    def delete_item(self, name):
        if name not in self.active.children:
            print("Item does not exist.")
        else:
            del self.active.children[name]

    def move_to(self, name):
        if name == "..":
            if self.active.parent:
                self.active = self.active.parent
        elif name in self.active.children and self.active.children[name].is_folder:
            self.active = self.active.children[name]
        else:
            print("Cannot navigate to the specified folder.")

    def show_path(self):
        path = []
        node = self.active
        while node.parent:
            path.append(node.label)
            node = node.parent
        print("/" + "/".join(reversed(path)))

    def start_shell(self):
        print("Beginner File System Shell - Type 'guide' for help")
        while True:
            try:
                entry = input("$ ").strip().split()
            except EOFError:
                break
            if not entry:
                continue

            cmd, *args = entry

            if cmd == "exit":
                break
            elif cmd == "guide":
                print("Available: folder [name], file [name], list, remove [name], go [name], path, exit")
            elif cmd == "folder" and args:
                self.make_folder(args[0])
            elif cmd == "file" and args:
                self.make_file(args[0])
            elif cmd == "list":
                self.list_items()
            elif cmd == "remove" and args:
                self.delete_item(args[0])
            elif cmd == "go" and args:
                self.move_to(args[0])
            elif cmd == "path":
                self.show_path()
            else:
                print("Unknown or invalid command.")


if __name__ == "__main__":
    fs = SimpleFileSystem()
    fs.start_shell()
