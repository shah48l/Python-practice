"""
Adapter Pattern (Structural Design Pattern)
============================================
Purpose:
    Allows incompatible interfaces to work together by wrapping an existing
    class (the "adaptee") with a new class (the "adapter") that exposes the
    expected interface (the "target").

When to use:
    - You want to use an existing class but its interface doesn't match
      the one your code expects.
    - You're integrating third-party / legacy code that you can't modify.

Key participants:
    Target    → MediaPlayer (the interface the client expects)
    Adaptee   → VLCPlayer, MP4Player (the classes with incompatible methods)
    Adapter   → VLCAdapter, MP4Adapter (translates Target calls → Adaptee calls)

Relationship used:
    Composition ("has-a"), NOT inheritance ("is-a").
    Each adapter *holds* an adaptee instance and delegates calls to it.
"""

from abc import ABC, abstractmethod


# ── TARGET: the common interface every media player must follow ──
class MediaPlayer(ABC):
    @abstractmethod
    def play(self, filename: str) -> None:
        """Play the given media file."""
        pass


# ── ADAPTEES: third-party classes whose interfaces we can NOT change ──
class VLCPlayer:
    def play_vlc(self, filename: str) -> None:
        print(f"VLC playing: {filename}")


class MP4Player:
    def play_mp4(self, filename: str) -> None:
        print(f"MP4 player playing: {filename}")


# ── ADAPTERS: bridge between Target interface and Adaptee methods ──
class VLCAdapter(MediaPlayer):
    """Wraps VLCPlayer so it can be used wherever MediaPlayer is expected."""

    def __init__(self, vlc_player: VLCPlayer):
        self._adaptee = vlc_player          # composition: hold the adaptee

    def play(self, filename: str) -> None:
        self._adaptee.play_vlc(filename)    # translate play() → play_vlc()


class MP4Adapter(MediaPlayer):
    """Wraps MP4Player so it can be used wherever MediaPlayer is expected."""

    def __init__(self, mp4_player: MP4Player):
        self._adaptee = mp4_player          # composition: hold the adaptee

    def play(self, filename: str) -> None:
        self._adaptee.play_mp4(filename)    # translate play() → play_mp4()


# ── CLIENT CODE: works only with the Target interface (MediaPlayer) ──
# BUG-FIX: this function was previously indented inside MP4Adapter,
#           making it an accidental method instead of a standalone function.
def play_media(player: MediaPlayer, filename: str) -> None:
    """Client function — it never knows which concrete player is underneath."""
    player.play(filename)


# ── USAGE ──
vlc = VLCAdapter(VLCPlayer())
mp4 = MP4Adapter(MP4Player())

play_media(vlc, "movie.avi")   # VLC playing: movie.avi
play_media(mp4, "clip.mp4")    # MP4 player playing: clip.mp4
        
