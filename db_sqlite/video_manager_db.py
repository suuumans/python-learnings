
import sqlite3

conn = sqlite3.connect('video_manager.db')
cursor = conn.cursor()

cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY,
        NAME TEXT NOT NULL,
        time TEXT NOT NULL
    )
''')

def list_all_videos():
    print("\n")
    print("*" * 50)
    cursor.execute("SELECT * FROM videos")
    videos = cursor.fetchall()
    for video in videos:
        print(f"ID: {video[0]}, Name: {video[1]}, Time: {video[2]}")
    
    print("\n")
    print("*" * 50)
    

def add_video(name, time):
    cursor.execute("INSERT INTO videos (NAME, time) VALUES (?, ?)", (name, time))
    conn.commit()
    print("Video added successfully!")

def update_video(video_id, name, time):
    cursor.execute("UPDATE videos SET NAME = ?, time = ? WHERE id = ?", (name, time, video_id))
    conn.commit()
    print("Video updated successfully!")

def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    conn.commit()
    print("Video deleted successfully!")
    

def main():
    while True:
        print("\n Video Manager app with DB")
        print("------------------------*****------------------------")
        print("1. List all videos")
        print("2. Add a video")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Exit the application")
        choice = input("Please select an option: ")

        if choice == "1":
            list_all_videos()
        elif choice == "2":
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_video(name, time)
        elif choice == "3":
            video_id = input("Enter the video ID to update: ")
            name = input("Enter the new video name: ")
            time = input("Enter the new video time: ")
            update_video(video_id, name, time)
        elif choice == "4":
            video_id = input("Enter the video ID to delete: ")
            delete_video(video_id)
        elif choice == "5":
            print("Exiting the application...")
            break
        else:
            print("Invalid option. Please try again.")

    conn.close()

if __name__ == "__main__":
    main()

        # match choice:
        #     case "1":
        #         list_all_videos()
        #     case "2":
        #         add_video()
        #     case "3":
        #         update_video()
        #     case "4":
        #         delete_video()
        #     case "5":
        #         print("Exiting the application...")
        #         break
        #     case _:
        #         print("Invalid option. Please try again.")

# Execute the main function if the script is executed directly