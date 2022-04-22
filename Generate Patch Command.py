#
#	Generate patch command
#	Usage: Make a selection in HEX view then run this script
#	Ray <ray@rayps.com> - github.com/rayps
#

doc = Document.getCurrentDocument()
seg = doc.getCurrentSegment()
start, end = doc.getSelectionAddressRange()
bytes = [seg.readByte(addr) for addr in range(start, end)]
bytes = "".join(fr"\x{i:x}" for i in bytes)
offset = doc.getFileOffsetFromAddress(start)
count = len(bytes)
path = doc.getExecutableFilePath()

template = 'printf "%s" | dd of="%s" bs=1 seek="%s" count="%s" conv=notrunc'
command = template % (bytes, path, offset, count)

print(command)

command_escaped = command.replace("\\x", "\\\\x")
os.system(f"echo '{command_escaped}' | pbcopy")

