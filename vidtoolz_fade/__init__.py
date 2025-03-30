import vidtoolz
import os
import subprocess


def get_length(filename):
    result = subprocess.run(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "default=noprint_wrappers=1:nokey=1",
            filename,
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    return float(result.stdout)


def determine_output_path(input_file, output_file):
    input_dir, input_filename = os.path.split(input_file)
    name, _ = os.path.splitext(input_filename)

    if output_file:
        output_dir, output_filename = os.path.split(output_file)
        if not output_dir:  # If no directory is specified, use input file's directory
            return os.path.join(input_dir, output_filename)
        return output_file
    else:
        return os.path.join(input_dir, f"{name}_fade.mp4")


def apply_fade_effect(video, output_file, fadetype="in", duration=2):
    try:
        # Check if the input file exists
        if not os.path.exists(video):
            raise FileNotFoundError(f"Input file '{video}' not found.")

        starttime = 0
        if fadetype == "out":
            length = get_length(video)
            starttime = length - duration

        afadetype = f"fade=t={fadetype}:st={starttime}:d={duration}"
        # Define the FFmpeg command
        command = [
            "ffmpeg",
            "-i",
            video,
            "-vf",
            afadetype,
            "-c:a",
            "copy",
            output_file,
        ]

        # ffmpeg -i input.mp4 -vf "fade=t=in:st=0:d=2" -c:a copy output.mp4

        # Execute the command
        result = subprocess.run(command, capture_output=True, text=True)

        # Check for errors during FFmpeg execution
        if result.returncode != 0:
            raise RuntimeError(f"FFmpeg error: {result.stderr}")

        print(f"Video trimmed successfully! Output saved to '{output_file}'.")

    except FileNotFoundError as fnfe:
        print(f"Error: {fnfe}")
    except ValueError as ve:
        print(f"Error: {ve}")
    except RuntimeError as re:
        print(f"Error: {re}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return output_file


def create_parser(subparser):
    parser = subparser.add_parser(
        "fade", description="Add fade in and out for a video using ffmpeg"
    )
    # Add subprser arguments here.
    parser.add_argument("video", help="Path to the input video file.")
    parser.add_argument(
        "-f",
        "--fadetype",
        choices=["in", "out"],
        default="in",
        help="Type of fade effect to apply. Default: in",
    )
    parser.add_argument(
        "-d",
        "--duration",
        type=float,
        default=2,
        help="Duration of the fade effect in seconds. (Default 2)",
    )
    parser.add_argument(
        "-o",
        "--output",
        default=None,
        help="Path for the output video file. Defaults to 'input_name_fade.mp4'.",
    )
    return parser


class ViztoolzPlugin:
    """Add fade in and out for a video using ffmpeg"""

    __name__ = "fade"

    @vidtoolz.hookimpl
    def register_commands(self, subparser):
        self.parser = create_parser(subparser)
        self.parser.set_defaults(func=self.run)

    def run(self, args):
        output = determine_output_path(args.video, args.output)
        iret = apply_fade_effect(args.video, output, args.fadetype, args.duration)
        print(f"{output} written.")

    def hello(self, args):
        # this routine will be called when "vidtoolz "fade is called."
        print("Hello! This is an example ``vidtoolz`` plugin.")


fade_plugin = ViztoolzPlugin()
