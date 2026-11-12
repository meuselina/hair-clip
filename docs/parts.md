# Parts list

Everything that goes into the clip, with what I've learned about each part.

| Part | Status | Notes |
|---|---|---|
| LILYGO T-Display-S3 (non-touch) | ✅ have it | ESP32-S3, 1.9" ST7789 LCD, 320 × 170 px, two buttons, USB-C, built-in LiPo charger |
| LiPo battery, 3.7 V | 🔄 searching | The first one I ordered (3300 mAh) is far too big and heavy for a hair clip. Looking for roughly 400–600 mAh, max. ~6 mm thick, with a JST-GH 1.25 mm 2-pin connector (check the polarity before plugging in!) |
| Metal hair clip blank | ⏳ to order | Gets glued or clipped into the case |
| Pearls and small flowers | ⏳ to order | Decoration around the front rim of the case |
| 3D-printed case | ⏳ to design | See the roadmap in the README |
| USB-C cable (data, not charge-only) | ✅ have it | A charge-only cable is the classic reason the CIRCUITPY drive doesn't show up |

## Things to check when choosing a battery

- **Size first:** the battery sits behind the board, so its footprint should be no bigger than the board itself.
- **Connector:** the board uses JST-GH 1.25 mm. Many cheap LiPos ship with a different plug (JST-PH 2.0 mm), which won't fit.
- **Polarity:** red = +, black = −. Some batteries have the wires swapped compared to the board's socket.
- **Protection circuit:** pick a cell with a built-in protection board (over-discharge / short circuit), since it will be worn on my head.
