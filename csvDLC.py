import deeplabcut


videopath=r'Z:\DLC\DLC_Analysis\Mouse59\50pct\Session19_hs2'
deeplabcut.analyze_videos_converth5_to_csv(videopath, videotype='.avi')