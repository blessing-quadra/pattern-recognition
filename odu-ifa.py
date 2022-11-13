
import importlib
text2speech = importlib.import_module("text2speech")
outcome = [
    # (faceup, facedown, meaning)
    (4, 4, "The oracle extends its greetings to you. As sweetness, never depart from honey, so shall your life be sweet. Something good is coming your way sooner. The gods beseech you to ensure you treat everybody well. The good thing may come in disguise, so be careful."),
    (5, 3, "The oracle is excited to speak with you. The gods are giving you assurance, that something good will locate you , before the end of today. Make sure you make everybody that comes your way happy today. Peace, be unto you."),
    (3, 5, "The oracle extends its greetings to you. You desire for something good but you are not sure if the thing will come to pass. The gods are giving you assurance now that it will come to pass. "),
    (6, 2, "The character of consciousness, or the inner essence of consciousness. The gods beseach you to be careful and conscious of somethings that will start happening in your life soon. The gods wants to reveal some hidden secret to you, so be at alert."),
    (2, 6, "You are entering into a new dispensation. It's either a new opportunity or a new partnership. Ensure you value everybody that comes your way, because the opportunity will come in disguise. The gods greet you."),
    (7, 1, "Someone promised to do something for you. You wish the promise get fulfiled but some powers are also working against it. Be prepared, because, by this time next two weeks, the long awaited promise will be fulfilled."),
    (1, 7, "The gods are excited to speak with you. Before you leave the gods presence. Ask for three things. The gods are ready to surprise you. Before the end of this month, you will start receiving what you asked for."),
    (8, 0, "The gods can see the manifestation of pure light before you. It is the expansion of light from source outward. One door will open for you soon. Make sure you value everybody that comes your way, because the door will be open through a way, that you don't expect. Peace be unto you."),
    (0,8, "Good things shall locate you this month. The gods knows your heart desires even when you don't say it. All your heart desires will be granted.")
]

def outputMapper(faceup, facedown):
    output = (int(faceup), int(facedown))
    result = list(filter(lambda x: x[0]==output[0] and x[1]==output[1], outcome))
    text2speech.readText(result[0][2])
    print(result[0][2])








# oponIfa = {
#     "ejiOgbe": {
#         "value": {"faceup": 8, "facedown": 8},
#         "meaning": ["Long life", "abundant blessings"]
#     },
#     "ofun": {
#         "value": {"faceup": 10, "facedown": 6},
#         "meaning": ["Spiritual wind-fall - Can sometimes means an ending"]
#     },
#     "irosun": {
#         "value": {"faceup": 4, "facedown": 12},
#         "meaning": ["Ancestral lineage", "Charity"]
#     },
#     "ogunda": {
#         "value": {"faceup": 3, "facedown": 13},
#         "meaning": ["Honesty", "Hard work", "Quarrels"]
#     },
#     "ejiOko": {
#         "value": {"faceup": 2, "facedown": 14},
#         "meaning": ["Ancestors", "strife among two"]
#     },
#     "okanran": {
#         "value": {"faceup": 1, "facedown": 15},
#         "meaning": ["Loss", "Struggle", "Need for persistence"]
#     },
#     "ejilaSebora": {
#         "value": {"faceup": 12, "facedown": 4},
#         "meaning": ["Loss", "Gossip", "Capriciousness"]
#     },
#     "owonrin": {
#         "value": {"faceup": 11, "facedown": 5},
#         "meaning": ["Leaving behind the past"]
#     },
#     "osa": {
#         "value": {"faceup": 9, "facedown": 7},
#         "meaning": ["Radical changes"]
#     },
#     "odi": {
#         "value": {"faceup": 7, "facedown": 9},
#         "meaning": ["Completion", "Reaping what was sown"]
#     },
#     "obara": {
#         "value": {"faceup": 6, "facedown": 10},
#         "meaning": ["Moneytary gain"]
#     },
#     "ose": {
#         "value": {"faceup": 5, "facedown": 11},
#         "meaning": ["Sweetness", "abundance"]
#     },
#     "ika": {
#         "value": {"faceup": 13, "facedown": 3},
#         "meaning": ["Sickness", "Change"]
#     },
#     "oturupon": {
#         "value": {"faceup": 14, "facedown": 2},
#         "meaning": ["Courage", "Humility"]
#     },
#     "ofunKanran": {
#         "value": {"faceup": 15, "facedown": 1},
#         "meaning": ["Peace", "Knowledge through study"]
#     },
#     "irete": {
#         "value": {"faceup": 16, "facedown": 0},
#         "meaning": ["Oppression", "Pressure"]
#     },
#     "opira": {
#         "value": {"faceup": 0, "facedown": 16},
#         "meaning": ["Ogboni", "Earth"]
#     }
# }