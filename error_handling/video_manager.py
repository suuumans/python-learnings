
# this video_manager.py file is a Python module that provides 
# functions for managing a list of videos.
# It includes functions to load video data from a file, save the data to the file, 
# list all videos, add a new video, update an existing video, and delete a video.

import json

def load_data():
  """
  This function loads video data from a file named 'youtube.txt'.
  If the file doesn't exist, it starts with an empty list of videos.
  """
  try:
    with open('youtube.txt', 'r') as file:
      # If the file exists, read the video data (which is in JSON format).
      return json.load(file)
  except FileNotFoundError:
    # If the file doesn't exist, tell the user and return an empty list.
    print("File not found. A new file will be created when you add your first video.")
    return []
  

def save_data_helper(videos):
  """
  This function saves the current list of videos to the 'youtube.txt' file.
  It overwrites the file with the new video data.
  """
  with open('youtube.txt', 'w') as file:
    # Save the videos list to the file in JSON format.
    json.dump(videos, file)

def list_all_videos(videos):
  """
  This function displays all the videos in the 'videos' list.
  If there are no videos, it tells the user to add some.
  """
  print("\n")
  print("*" * 50) # Print a line of stars for visual separation
  if not videos:
    # If the videos list is empty, print this message.
    print("No videos found. Please add some videos using option '2' first!")
  else:
    # If there are videos, loop through them and print their details.
    for index, video in enumerate(videos, start=1):
      print(f"{index}. {video['name']}, Duration: {video['time']}")
  print("\n")
  print("*" * 50) # Print another line of stars

def add_video(videos):
  """
  This function lets the user add a new video to the list.
  It asks for the video's name and duration, then saves the updated list.
  """
  name = input("Enter the title of the video: ") # Ask for the video name
  time = input("Enter video time:") # Ask for the video duration
  videos.append({ # Add the new video as a dictionary to the list
    "name": name,
    "time": time
  })
  save_data_helper(videos) # Save the updated list to the file
  print(f"Video '{name}' added successfully!") # Tell the user the video was added
  return videos

def update_video(videos):
  """
  This function lets the user update an existing video's details.
  It shows the list of videos, asks which one to update, and then asks for the new details.
  """
  list_all_videos(videos) # Show the current list of videos
  if not videos: # If there are no videos, exit the function
    return
  index = int(input("Enter the index of the video to update: ")) # Ask for the index of the video to update
  if 1 <= index <= len(videos): # Check if the index is valid
    name = input("Enter the new title of the video: ") # Ask for the new name
    time = input("Enter the new time of the video: ") # Ask for the new duration
    videos[index - 1] = { # Update the video at the specified index
      "name": name,
      "time": time
    }
    save_data_helper(videos) # Save the updated list
    print(f"Video at index {index} updated successfully!") # Tell the user the video was updated
  else:
    print("Invalid index. Please try again.") # Tell the user if the index was invalid

def delete_video(videos):
  """
  This function lets the user delete a video from the list.
  It shows the list of videos, asks which one to delete, and then removes it.
  """
  list_all_videos(videos) # Show the current list of videos
  if not videos: # If there are no videos, exit the function
    return
  index = int(input("Enter the index of the video to delete: ")) # Ask for the index of the video to delete
  if 1 <= index <= len(videos): # Check if the index is valid
    deleted_video = videos.pop(index - 1) # Remove the video at the specified index
    save_data_helper(videos) # Save the updated list
    print(f"Video '{deleted_video['name']}' deleted successfully!") # Tell the user which video was deleted
  else:
    print("Invalid index. Please try again.") # Tell the user if the index was invalid

def main():
  """
  This is the main function that runs the video manager program.
  It loads the video data, shows the menu, and handles user choices.
  """
  videos = load_data() # Load the video data from the file
  while True: # Keep running until the user chooses to exit
    print("\n Video Manager | Choose an option")
    print("------------------------*****------------------------") # Print a line for visual separation
    print("0. Show menu")
    print("1. List a favorite videos")
    print("2. Add a video")
    print("3. upadate a video details")
    print("4. Delete a video")
    print("5. Exit the application")
    choice = input("Please select an option: ") # Ask the user to choose an option

    match choice: # Check the user's choice
      case "1":
        list_all_videos(videos) # List all videos
      case "2":
        add_video(videos) # Add a new video
      case "3":
        update_video(videos) # Update a video
      case "4":
        delete_video(videos) # Delete a video
      case "5":
        print("Exiting the application...") # Tell the user the program is exiting
        break # Exit the loop
      case _:
        print("Invalid choice. Please select a valid option.") # Tell the user if they entered an invalid choice

if __name__ ==  "__main__":
  main() # Run the main function if the script is executed directly
