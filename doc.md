Created invoice-generator.html — a single-file invoice generator with:

Business & client info fields
Auto-incrementing invoice number field, date & due date (defaults to today / +30 days)
Dynamic line items (description, qty, rate) with add/remove and live amount calc
Tax rate input that auto-calculates tax and grand total
Payment terms/notes section
Live preview panel styled as a clean professional invoice
"Print / Save as PDF" button with print CSS that hides the form and shows only the invoice
Just open the file in a browser, fill in the fields on the left, and the invoice preview updates live on the right. Click "Print / Save as PDF" and choose "Save as PDF" in the print dialog.


Created snake.html — a complete single-file Snake game with:

Smooth interpolated movement (no choppy grid-jumps)
Score + persistent high score (localStorage)
3 speed levels (Slow/Normal/Fast dropdown)
Pause button + pause overlay (also spacebar)
Game-over screen with score, new-high-score flag, and restart
Particle burst effect on eating food
Retro neon-green-on-black theme with glow/shadow effects
Keyboard (arrows/WASD), on-screen touch D-pad, and swipe controls for mobile
"DotnetAbhishekAI" branding in the header and footer
You can open it directly in a browser to play — it's already showing in the preview panel.

Created csv-visualizer.html — a self-contained dashboard with:

Drag-and-drop/upload CSV input with custom parser (handles quoted fields, commas, newlines)
Type detection per column (number, date, boolean, string) shown as badges
Preview table (first 15 rows) with sticky header
Per-column stats: count, missing, average/min/max/sum for numbers, unique values + most common for text, date range for dates
Chart builder: pick X/Y axes, toggle bar/line/pie, aggregates by grouping X (sum if Y is numeric, count otherwise)
Dark dashboard theme, Chart.js via CDN, "dotnetabhishekai" brand tag in header and footer
Open it in a browser and drop a CSV in to try it out.

Created sample-data.csv — 20 rows with a mix of column types to exercise the visualizer:

Date → date-typed column
Region, Product, Category → strings (good for X-axis grouping)
UnitsSold, Revenue → numbers (good for Y-axis, stats)
InStock → boolean
Open csv-visualizer.html and drop this file in — try X=Region/Category with Y=Revenue for bar/pie charts, or X=Date with Y=UnitsSold for a line chart.