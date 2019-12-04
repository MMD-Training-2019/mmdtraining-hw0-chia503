# HW0 - Python Learning
HW0希望確保同學們能夠執行機器學習所需的一些基本操作。

### Q1 出現數字統計
 1. 讀取words.txt中的所有英文單字,英文單字之間皆由<space>做分隔
 2. 按照單字出現的順序,給予編號(0, 1, 2 ...)。 (不要跳號)
 3. 計算單字出現的次數。
 4. 將得到編號和次數,由**單字出現在words.txt的順序**輸出至Q1.txt,最後一行不要換行,每一行皆為:<單字><space><編號><space><出現次數>
 5. **Ntu, ntu 為不同單字**

### Q1 出現單字統計 - 輸出範例
words.txt 

    ntu ml mlds ml ntu ntuee
Q1.txt :(輸出的檔案)

    ntu 0 2
    ml 1 2
    mlds 2 1
    ntuee 3 1

### Q2 圖片淡化
 1. 讀取 sumi.jpg
 2. 將每個pixel的RGB數值都減半(ex: (122, 244, 245)->(61, 122, 122)),再將圖片輸出為 Q2.jpg
 3. RGB數值記得要去掉小數點!(無條件捨去)

### Q2 圖片淡化 - 輸出範例
![原本的範例](https://github.com/MMD-Training-2019/hw0-test/blob/master/example/west.PNG)

# Usage
To start working on this assignment, you should clone this repository into your local machine by using the following command.

    git clone https://github.com/MMD-Training-2019/hw0-<username>.git
Note that you should replace `<username>` with your own GitHub username.

### Dataset
In the starter code of this repository, we have provided `word.txt` and `sumi.jpg` in `dataset` folder.

# Submission Rules
### Deadline
2019/12/15 (Sun.) 12:00 AM

### Academic Honesty
-   If you refer to some parts of the public code, you are required to specify the references in your report (e.g. URL to GitHub repositories).      

### Submission Format
Aside from your own Python scripts and model files, you should make sure that your submission includes *at least* the following files in the root directory of this repository:
 1.   `hw0_<your_name>.pdf`  
 2.    `q1.py`
可以執行並且產生`Q1.txt`
 3.    `q2.py`
可以執行並且產生`Q2.jpg`

# Q&A
If you have any problems related to HW0, you may
- Contact us by messenger
