import os
import imageio


def splitIntoFrames(dirPath, targetFormat):
    reader = imageio.get_reader(os.path.abspath(fileName))
    newDir = dirPath+"\\"+fileName+" (frames)"
    if(not os.path.exists(newDir)):
        os.makedirs(newDir)
    frameNumber = 1
    for frame in reader:
        writer = imageio.get_writer(
            newDir+"\\"+str(frameNumber)+targetFormat)
        writer.append_data(frame)
        print(f"Separating frames... {frameNumber} completed")
        frameNumber += 1
    print(f'Converting complete!{frameNumber}/{frameNumber}')
    writer.close()


fileName = input(
    "Name of the file inside this directory (include format: MP4, AVI, etc.): ")

if(os.path.exists(fileName)):
    folderPath = os.path.dirname(os.path.abspath(fileName))
    splitIntoFrames(folderPath, ".jpg")
else:
    input("File does not exist in this folder! (make sure you include the format: MP4, AVI, etc.)")
