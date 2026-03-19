# Hàm lấy tên file: muabui.mp3
def get_filename(path):
    parts = path.split("\\")   # tách theo dấu \
    return parts[-1]           # lấy phần cuối


# Hàm lấy tên bài hát: muabui
def get_song_name(path):
    filename = get_filename(path)   # gọi lại hàm trên
    parts = filename.split(".")     # tách theo dấu .
    return parts[0]                 # lấy phần trước dấu .


# Test
path = "d:\\music\\muabui.mp3"

print(get_filename(path))   # muabui.mp3
print(get_song_name(path))  # muabui