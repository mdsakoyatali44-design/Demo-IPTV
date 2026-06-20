import re
import requests

# আপনার ইউটিউব লাইভ ভিডিওর আইডি
video_id = "gxxvnM4-PTU"
youtube_url = f"https://www.youtube.com/watch?v={video_id}"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36"
}

try:
    response = requests.get(youtube_url, headers=headers)
    html = response.text
    
    # ইউটিউব পেজ থেকে আসল .m3u8 লিংকটি খোঁজা হচ্ছে
    matches = re.search(r'"hlsManifestUrl":"([^"]+)"', html)
    
    if matches:
        m3u8_url = matches.group(1).replace(r"\/", "/")
        
        # M3U8 প্লেলিস্টের লেখা তৈরি করা হচ্ছে
        m3u_content = f"""#EXTM3U
#EXTINF:-1 tvg-id="GermanyvsIvoryCoast" tvg-name="GERMANY vs IVORY COAST Live" tvg-logo="https://i.ytimg.com/vi/{video_id}/maxresdefault_live.jpg" group-title="Sports Live",🔴LIVE: GERMANY vs IVORY COAST
{m3u8_url}"""
        
        # ফাইল হিসেবে সেভ করা হচ্ছে
        with open("live.m3u", "w", encoding="utf-8") as f:
            f.write(m3u_content)
        print("M3U Playlist updated successfully!")
    else:
        print("Live Stream Link Not Found!")
except Exception as e:
    print(f"Error: {e}")
