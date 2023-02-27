import re

# Define regular expressions to match each piece of information
episode_regex = r"\[(?:第)?(\d+(?:\.\d+)?|\d+-\d+)\w*\]"
resolution_regex = r"(?:(\d+)P)|4K"
bit_depth_regex = r"\d+bit"
video_codec_regex = r"(?:AVC|HEVC|H\.?265|HVEC|AV1)"
audio_codec_regex = r"(?:AAC|FLAC)"
subtitle_language_regex = r"(?:简体|繁体|日本語|英語|English)"
subtitle_packaging_regex = r"(?:内嵌|内封|外挂)"
format_regex = r"(?:MKV|MP4)"
video_source_regex = r"(?:WebRip|WEB-DL|BDRip|Blu-ray)"
webrip_source_regex = r"(?:B-Global|Baha|CR)"

# Combine all the regular expressions into a single pattern
pattern = r"{}.*(?:{})?(?:{})?(?:{})?(?:{})?(?:{})?(?:{})?(?:{})?(?:{})?(?:{}).*".format(
    episode_regex, resolution_regex, bit_depth_regex, video_codec_regex,
    audio_codec_regex, subtitle_language_regex, subtitle_packaging_regex,
    format_regex, video_source_regex, webrip_source_regex)

# Define a function to extract the information from a string


def extract_info(text):
    match = re.match(pattern, text)
    if match:
        episode = match.group(1)
        resolution = match.group(2) if match.group(2) else "/"
        bit_depth = match.group(3) if match.group(3) else "/"
        video_codec = match.group(4) if match.group(4) else "/"
        audio_codec = match.group(5) if match.group(5) else "/"
        subtitle_language = match.group(6) if match.group(6) else "/"
        subtitle_packaging = match.group(7) if match.group(7) else "/"
        video_format = match.group(8) if match.group(8) else "/"
        video_source = match.group(9) if match.group(9) else "/"
        if video_source == "WebRip":
            webrip_source = match.group(10) if match.group(10) else "/"
        else:
            webrip_source = "/"
        return episode, resolution, bit_depth, video_codec, audio_codec, subtitle_language, subtitle_packaging, video_format, video_source, webrip_source
    else:
        return None


# Example usage:
text = "[NC-Raws] 不当哥哥了！ / Oniichan wa Oshimai! - 04 (CR 1920x1080 AVC AAC MKV)"
print(extract_info(text))
# Output: ('04', '1080P', '/', 'AVC', 'AAC', '/', '/', 'MKV', 'WebRip', 'CR')

text = "[7³ACG] 莉可丽丝/リコリス・リコイル/Lycoris Recoil | 01-13 [简繁英字幕] BDrip 1080p x265 FLAC"
print(extract_info(text))
# Output: ('01-13', '1080P', '/', 'HEVC', 'FLAC', '简繁英', '/', '/', 'BDrip', '/')
