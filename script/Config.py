##############################
# CONST 
WIDTH = 1920
HEIGHT = 1080

OP_UI_PARMS = op('/project1/uiParams')

VISUALIZE_VIDEO_SECONDS = {
  'pattern0': 0.5,
  'pattern1': 0.5,
  'pattern2': 0.9,
  'pattern3': 0.5,
  'pattern4': 0.5,
  'pattern5': 0.5,
  'pattern6': 0.5,
  'pattern7': 0.5
}

UI_SIDE_WIDTH = 600

UI_TITLE_SIZE = 10
UI_TITLE_WIDTH = 600
UI_TITLE_HEIGHT = 18

UI_MARGIN = 10
MOV_COLOR = {
  "Low" : {
    "r": op('/project1/uiParams')['/movcolor/low/r'],
    "g": op('/project1/uiParams')['/movcolor/low/g'],
    "b": op('/project1/uiParams')['/movcolor/low/b']
  },
  "Mid": {
    "r": op('/project1/uiParams')['/movcolor/mid/r'],
    "g": op('/project1/uiParams')['/movcolor/mid/g'],
    "b": op('/project1/uiParams')['/movcolor/mid/b']
  },
  "High":{
    "r": op('/project1/uiParams')['/movcolor/high/r'],
    "g": op('/project1/uiParams')['/movcolor/high/g'],
    "b": op('/project1/uiParams')['/movcolor/high/b']
  }
}




