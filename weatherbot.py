#!/usr/bin/env python3
"""
MansionNet Weather Bot
A simple IRC bot that provides weather information using the Open-Meteo API
"""

import socket
import ssl
import requests
import time
from datetime import datetime

class WeatherBot:
    def __init__(self):
        self.server = "irc.server.com"
        self.port = 6697
        self.nickname = "WeatherBot"
        self.channels = ["#help","#welcome"]
        
        self.ssl_context = ssl.create_default_context()
        self.ssl_context.check_hostname = False
        self.ssl_context.verify_mode = ssl.CERT_NONE

    def connect(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.irc = self.ssl_context.wrap_socket(sock)
        
        print(f"Connecting to {self.server}:{self.port}...")
        self.irc.connect((self.server, self.port))
        
        self.send(f"NICK {self.nickname}")
        self.send(f"USER {self.nickname} 0 * :MansionNet Weather Information Bot")
        
        buffer = ""
        registered = False
        while not registered:
            try:
                temp = self.irc.recv(2048).decode("UTF-8")
                print("Received:", temp)
                buffer += temp
                
                if "PING" in buffer:
                    ping_token = buffer[buffer.find("PING"):].split()[1]
                    self.send(f"PONG {ping_token}")
                    print(f"Responded to PING with: PONG {ping_token}")
                
                if "001" in buffer:
                    print("Successfully registered!")
                    registered = True
                    break
                    
                if "Closing Link" in buffer or "ERROR" in buffer:
                    print("Registration failed, retrying...")
                    time.sleep(5)
                    return False
                    
            except UnicodeDecodeError:
                buffer = ""
                continue
            except Exception as e:
                print(f"Error during registration: {str(e)}")
                time.sleep(5)
                return False
        
        for channel in self.channels:
            print(f"Joining channel {channel}")
            self.send(f"JOIN {channel}")
            time.sleep(1)

        return True

    def send(self, message):
        print(f"Sending: {message}")
        self.irc.send(bytes(f"{message}\r\n", "UTF-8"))

    def send_message(self, target, message):
        self.send(f"PRIVMSG {target} :{message}")

    def get_coordinates(self, city):
        try:
            url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=en&format=json"
            response = requests.get(url)
            data = response.json()
            
            if response.status_code == 200 and data.get('results'):
                location = data['results'][0]
                return {
                    'lat': location['latitude'],
                    'lon': location['longitude'],
                    'name': location['name'],
                    'country': location['country']
                }
            return None
        except Exception as e:
            print(f"Geocoding error: {str(e)}")
            return None

    def get_weather(self, city):
        try:
            location = self.get_coordinates(city)
            if not location:
                return f"Could not find location: {city}"

            url = f"https://api.open-meteo.com/v1/forecast?latitude={location['lat']}&longitude={location['lon']}&current=temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code"
            response = requests.get(url)
            
            if response.status_code == 200:
                data = response.json()
                current = data['current']
                
                weather_codes = {
                    0: "Clear sky",
                    1: "Mainly clear", 2: "Partly cloudy", 3: "Overcast",
                    45: "Foggy", 48: "Depositing rime fog",
                    51: "Light drizzle", 53: "Moderate drizzle", 55: "Dense drizzle",
                    61: "Slight rain", 63: "Moderate rain", 65: "Heavy rain",
                    71: "Slight snow", 73: "Moderate snow", 75: "Heavy snow",
                    77: "Snow grains",
                    80: "Slight rain showers", 81: "Moderate rain showers", 82: "Violent rain showers",
                    85: "Slight snow showers", 86: "Heavy snow showers",
                    95: "Thunderstorm", 96: "Thunderstorm with hail", 99: "Thunderstorm with heavy hail"
                }
                
                weather_desc = weather_codes.get(current['weather_code'], "Unknown")
                
                BOLD = '\x02'
                COLOR = '\x03'
                RESET = '\x0F'
                
                TEXT = '07,01'  # Orange on black
                
                return (f"{COLOR}{TEXT}{BOLD}{location['name']}, {location['country']}{RESET} "
                       f"{COLOR}{TEXT}【{weather_desc}】 "
                       f"▸ {current['temperature_2m']}°C "
                       f"❋ {current['relative_humidity_2m']}% "
                       f"⟳ {current['wind_speed_10m']} km/h{RESET}")
            else:
                return f"Could not fetch weather data for {city}"
                
        except Exception as e:
            return f"Error fetching weather data: {str(e)}"

    def run(self):
        while True:
            try:
                if self.connect():
                    buffer = ""
                    
                    while True:
                        try:
                            buffer += self.irc.recv(2048).decode("UTF-8")
                            lines = buffer.split("\r\n")
                            buffer = lines.pop()
                            
                            for line in lines:
                                print(line)
                                
                                if line.startswith("PING"):
                                    ping_token = line.split()[1]
                                    self.send(f"PONG {ping_token}")
                                
                                if "PRIVMSG" in line:
                                    parts = line.split()
                                    target_channel = parts[2]
                                    
                                    if target_channel in self.channels:
                                        sender = line.split("!")[0][1:]
                                        message = line.split("PRIVMSG")[1].split(":", 1)[1].strip()
                                        print(f"Received message from {sender} in {target_channel}: {message}")
                                        
                                        if message.startswith("!weather"):
                                            parts = message.split()
                                            if len(parts) > 1:
                                                city = " ".join(parts[1:])
                                                weather = self.get_weather(city)
                                                self.send_message(target_channel, weather)
                                            else:
                                                self.send_message(target_channel, "Usage: !weather <city>")
                                        
                                        elif message == "!help":
                                            help_msg = "MansionNet Weather Bot | Commands: !weather <city> - Get weather information for a city"
                                            self.send_message(target_channel, help_msg)
                                    
                        except UnicodeDecodeError:
                            buffer = ""
                            continue
                            
            except Exception as e:
                print(f"Error: {str(e)}")
                time.sleep(30)
                continue

if __name__ == "__main__":
    bot = WeatherBot()
    bot.run()
