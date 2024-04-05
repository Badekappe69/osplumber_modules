print("Preparing partitions!")
# Create Partitions And Make Filesystem

if_not_there_create_folder("tmp")

fdisk = open(path + "/tmp/fdisk.tab", "w")
fdisk.writelines("device: /dev/" + fs_json["device"] + "\n")
fdisk.writelines("\n")
    
index = 1
for p in fs_json["partitions"]:
    if index == 1: # /boot
        fdisk.writelines("/dev/" + fs_json["partitions"][p]["partition"] + " :  start=2048, size=" + fs_json["partitions"][p]["size"] + ", type=" + fs_json["partitions"][p]["type"] + "\n")
    else:
        fdisk.writelines("/dev/" + fs_json["partitions"][p]["partition"] + " :  size=" + fs_json["partitions"][p]["size"] + ", type=" + fs_json["partitions"][p]["type"] + "\n")
index=index+1
    
fdisk.close()

    exec_bash("wipefs -a " + "/dev/" + fs_json["device"])
    exec_bash("sfdisk " + "/dev/" + fs_json["device"] + " < " + path + "/tmp/fdisk.tab")

    exec_bash("sfdisk /dev/" + fs_json["device"] + " < " + path + "/tmp/fdisk.tab")

    print("Done preparing partitons!")