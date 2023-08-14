import os

folder_path = 'D:\\test\\train_1\\train\labels'
new_chars = '_wh'

# Kiểm tra xem đường dẫn thư mục có tồn tại hay không
if not os.path.exists(folder_path):
    print(f"Thư mục '{folder_path}' không tồn tại.")
else:
    # Lặp qua tất cả các tệp trong thư mục
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            old_path = os.path.join(folder_path, filename)
            file_name, file_extension = os.path.splitext(filename)
            
            # Kiểm tra nếu tên file có ít nhất 3 kí tự
            if len(file_name) >= 3:
                new_file_name = file_name[:-3] + new_chars + file_extension
                new_path = os.path.join(folder_path, new_file_name)
                
                # Thực hiện việc đổi tên
                os.rename(old_path, new_path)
                print(f"Đã đổi tên '{filename}' thành '{new_file_name}'")
            else:
                print(f"Không thể đổi tên '{filename}' do tên file quá ngắn.")
