import requests

def get_live_matches():
    try:
        url = "https://cricbuzz-cricket.p.rapidapi.com/series/v1/international"
        headers = {
            "X-RapidAPI-Key": "6a8ec70401msh7b164f32548fe9ap1a9bb9jsnda084dcf07e6",   # replace with your RapidAPI key
            "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Failed to fetch data. Status code: {response.status_code}"}
    except Exception as e:
        return {"error": str(e)}
