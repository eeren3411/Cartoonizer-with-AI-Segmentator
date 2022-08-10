# Cartoonizer-with-AI-Segmenter
AI-Segmented Cartoonizer. Can be used with your own segmenter. I dunno why I wrote segmentator to the title and I have no idea how to change it now.

# How to use?
0-) Install packages with pip
```
python -m pip install -r requirements.txt
```

1-) Initialize class with either a segmenter or a string "Human" to use automatically mediapipe selfie segmentation.

2-) Call run function with an image or an image path.
```
Note: In case of string input, I didn't check if its a path or not. 
If it's a string but not a path, program will crash.
```

3-) Use it?

# Why did I do this?
I thought it will be cool but it wasn't. Who could have knew that cv2 has a built in function for it? 

But the main reason behind this project was learning how to use github and it's already in github now so I won't take it down back.

# Maybe an example?

![robert](https://user-images.githubusercontent.com/77689346/183890251-b6b5da09-27a4-42fd-812c-6c005840b6df.jpg)

![output](https://user-images.githubusercontent.com/77689346/183890268-63137ecd-1d48-42bd-a86e-8f4e933fe1aa.jpg)

## Background cropped?

![output2](https://user-images.githubusercontent.com/77689346/183890335-0fc906ed-5208-4b61-bcec-fa2f1446114f.jpg)
