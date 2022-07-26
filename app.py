
from pytube import YouTube
import config


class YoutubeDownloader:

    def __init__(self, save_path, link, file_name):
        self.save_path = save_path
        self.link = link
        self.file_name = file_name

    def download_single_video(self):
        try:
            yt = YouTube(self.link)
        except:
            print("Connection Error")
            
        mp4files = yt.filter('mp4')

        yt.set_filename(self.file_name)

        d_video = yt.get(mp4files[-1].extension, mp4files[-1].resolution)
        try:
            # downloading the video
            d_video.download(self.save_path)
        except:
            print("Some Error!")

    def download_multiple_videos(self):

        # link of the video to be downloaded
        link = ["https://www.youtube.com/watch?v=xWOoBJUqlbI",
                "https://www.youtube.com/watch?v=xWOoBJUqlbI"
                ]

        for i in link:
            try:

                # object creation using YouTube
                # which was imported in the beginning
                yt = YouTube(i)
            except:

                # to handle exception
                print("Connection Error")

            # filters out all the files with "mp4" extension
            mp4files = yt.filter('mp4')

            # get the video with the extension and
            # resolution passed in the get() function
            d_video = yt.get(mp4files[-1].extension, mp4files[-1].resolution)
            try:
                # downloading the video
                d_video.download(self.save_path)
            except:
                print("Some Error!")
        print('Task Completed!')


def main():
    link_input = input("Put the link here:\n")
    link_file_name = input("Set file name: \n")
    youtube_downloader = YoutubeDownloader(
        config.DOWNLOAD_PATH, link_input, link_file_name)
    youtube_downloader.download_single_video()


if __name__ == "__main__":
    main()
