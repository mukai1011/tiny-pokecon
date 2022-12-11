# tiny-pokecon

cv2.VideoCaptureの画像をぬるぬる表示させるためのサンプル

## Summary

**tk.Canvas#afterで指定するミリ秒が、表示の更新にかかる時間よりも短い**場合にGUIの応答が悪くなることがわかった。[CaptureCanvas](./tiny_pokecon/view/capture_canvas.py)#__updateのafterを1などにすると顕著（簡易なアプリケーションなので、PCに十分なスペックがあればわからないかもしれない......）

そこで、描画の更新にかかる平均の時間を求めて、次回の描画の更新をこれよりも遅くする。手元の環境では、平均は15ms程度（60fps）におさまっている。
