from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from time import sleep
import numpy as np


html0 = """
<!DOCTYPE html>
<html>
<head>
	<link rel="stylesheet" href="style.css">
	<script>
		var colors = ["#ffb6b9", "#fae3d9", "#bbded6", "#d9d9f3"];
		var colorIndex = 0;
		function changeColor() {
			var col1 = document.getElementsByClassName("WEEK");
				if( colorIndex >= colors.length ) {
				    colorIndex = 0;
			}
			for(var i=0, len=col1.length; i<len; i++) {
				col1[i].style["background-color"] = colors[colorIndex];
			}
			var col2 = document.getElementsByClassName("TIME");
				if( colorIndex >= colors.length ) {
				    colorIndex = 0;
			}
			for(var i=0, len=col2.length; i<len; i++) {
				col2[i].style["background-color"] = colors[colorIndex];
			}
			colorIndex++;
		}
	</script>
	<title>
"""

html1 = """
	</title>
</head>
<body>
	<span style="margin:100px;">
	<button class="button" onclick="changeColor();" ><span>Change color</span></button>
	</span>
	
	<table class="table1" align="center" border="12" width="90%";>
		<tbody>
			<!-------------------------------------------------------------------------------------------------------------------------------->
			<tr>
				<th class="WEEK" id = "COLOR1"  width="10%">星期/區段</th>
				<th class="WEEK">一</th>
				<th class="WEEK">二</th>
				<th class="WEEK">三</th>
				<th class="WEEK">四</th>
				<th class="WEEK">五</th>
				<th class="WEEK">六</th>
				<th class="WEEK">日</th>
			</tr>
			<!-------------------------------------------------------------------------------------------------------------------------------->
			<tr valign="center" width="100px">
				<th class="REGION" style="height:auto;">
					<div class="block1" id="b1">
					<div class="block2">
						<table>
							<tr>
								<td rowspan="3" class="TIME">I</td>
								<td class="TIME">1</td>
								<td class="TIME">7:10<br>8:00</td>
							</tr>
							<tr>
								<td class="TIME">2</td>
								<td class="TIME">8:10<br>9:00</td>
							</tr>
							<tr>
								<td class="TIME">3</td>
								<td class="TIME">9:10<br>10:00</td>
							</tr>
						</table>
					</div>
					<div class="block2">
						<table width="55px">
							<tr>
								<td class="TIME">A</td>
								<td class="TIME">7:00<br>8:00</td>
							</tr>
								<td class="TIME">B</td>
								<td class="TIME">8:10<br>9:00</td>
							</tr>
						</table>
					</div>
					</div>				
				</th>
"""
html2 = """
			</tr>
			<!-------------------------------------------------------------------------------------------------------------------------------->
			<tr valign="center">
				<th class="REGION" style="height:auto;width:auto">
					<div class="block1" id="b2">
					<div class="block2">
						<table>
							<tr>
								<td rowspan="3" class="TIME">II</td>
								<td class="TIME">4</td>
								<td class="TIME">10:10<br>11:00</td>
							</tr>
							<tr>
								<td class="TIME">5</td>
								<td class="TIME">11:10<br>12:00</td>
							</tr>
							<tr>
								<td class="TIME">6</td>
								<td class="TIME">12:10<br>13:00</td>
							</tr>
						</table>
					</div>
					<div class="block2">
						<table width="55px">
							<tr>
								<td class="TIME">C</td>
								<td class="TIME">10:15<br>11:30</td>
							</tr>
							<tr>
								<td class="TIME">D</td>
								<td class="TIME">11:45<br>13:00</td>
							</tr>
						</table>
					</div>
					</div>				
				</th>
"""
html3 = """
			</tr>
			<!-------------------------------------------------------------------------------------------------------------------------------->
			<tr valign="center">
				<th class="REGION" style="height:auto;width:auto">
					<div class="block1" id="b3">
					<div class="block2">
						<table>
							<tr>
								<td rowspan="3" class="TIME">III</td>
								<td class="TIME">7</td>
								<td class="TIME">13:10<br>14:00</td>
							</tr>
							<tr>
								<td class="TIME">8</td>
								<td class="TIME">14:10<br>15:00</td>
							</tr>
							<tr>
								<td class="TIME">9</td>
								<td class="TIME">15:10<br>16:00</td>
							</tr>
						</table>
					</div>
					<div class="block2">
						<table width="55px">
							<tr>
								<td class="TIME">E</td>
								<td class="TIME">13:15<br>14:30</td>
							</tr>
							<tr>
								<td class="TIME">F</td>
								<td class="TIME">14:45<br>16:00</td>
							</tr>
						</table>
					</div>
					</div>				
				</th>
"""
html4 = """
			</tr>
			<!-------------------------------------------------------------------------------------------------------------------------------->
			<tr valign="center">
				<th class="REGION" style="height:auto;width:auto">
					<div class="block1" id="b4">
					<div class="block2">
						<table>
							<tr>
								<td rowspan="3" class="TIME">IV</td>
								<td class="TIME">10</td>
								<td class="TIME">16:10<br>17:00</td>
							</tr>
							<tr>
								<td class="TIME">11</td>
								<td class="TIME">17:10<br>18:00</td>
							</tr>
							<tr>
								<td class="TIME">12</td>
								<td class="TIME">18:10<br>19:00</td>
							</tr>
						</table>
					</div>
					<div class="block2">
						<table width="55px">
							<tr>
								<td class="TIME">G</td>
								<td class="TIME">16:15<br>17:30</td>
							</tr>
							<tr>
								<td class="TIME">H</td>
								<td class="TIME">17:45<br>19:00</td>
							</tr>
						</table>
					</div>
					</div>				
				</th>
"""
html5 = """
			</tr>
			<!-------------------------------------------------------------------------------------------------------------------------------->
			<tr valign="center">
				<th class="REGION" style="height:auto;width:auto">
					<div class="block1" id="b5">
					<div class="block2">
						<table>
							<tr>
								<td rowspan="3" class="TIME">V</td>
								<td class="TIME">13</td>
								<td class="TIME">19:10<br>20:00</td>
							</tr>
							<tr>
								<td class="TIME">14</td>
								<td class="TIME">20:10<br>21:00</td>
							</tr>
							<tr>
								<td class="TIME">15</td>
								<td class="TIME">21:10<br>22:00</td>
							</tr>
						</table>
					</div>
					<div class="block2">
						<table width="55px">
							<tr>
								<td class="TIME">I</td>
								<td class="TIME">19:15<br>20:30</td>
							</tr>
							<tr>
								<td class="TIME">J</td>
								<td class="TIME">20:45<br>22:00</td>
							</tr>
						</table>
					</div>
					</div>				
				</th>
"""
html6 = """
			</tr>
			<!-------------------------------------------------------------------------------------------------------------------------------->
		</tbody>
	</table>
	<script>
	var F1 = (function findH() {
				var table = document.getElementsByClassName("REGION");
				document.getElementById("b1").style.height= table[0].offsetHeight +"px";
				document.getElementById("b2").style.height= table[1].offsetHeight +"px";
				document.getElementById("b3").style.height= table[2].offsetHeight +"px";
				document.getElementById("b4").style.height= table[3].offsetHeight +"px";
				document.getElementById("b5").style.height= table[4].offsetHeight +"px";
			}());
	</script>
	<script>
	var off = 2;
	function findH1() {
		var table = document.getElementsByClassName("REGION");
		document.getElementById("b1").style.height= "120px";
		document.getElementById("b2").style.height= "120px";
		document.getElementById("b3").style.height= "120px";	
		document.getElementById("b4").style.height= "120px";
		document.getElementById("b5").style.height= "120px";
		document.getElementById("b1").style.height= table[0].offsetHeight -off +"px";
		document.getElementById("b2").style.height= table[1].offsetHeight -off +"px";
		document.getElementById("b3").style.height= table[2].offsetHeight -off +"px";		
		document.getElementById("b4").style.height= table[3].offsetHeight -off +"px";
		document.getElementById("b5").style.height= table[4].offsetHeight -off +"px";
	}
	setInterval(findH1,10);
	</script>
</body>
</html>
"""

O0 = np.array([['&nbsp;', '&nbsp;', '&nbsp;', '&nbsp;', '&nbsp;'],
              ['&nbsp;', '&nbsp;', '&nbsp;', '&nbsp;', '&nbsp;'],
              ['&nbsp;', '&nbsp;', '&nbsp;', '&nbsp;', '&nbsp;'],
              ['&nbsp;', '&nbsp;', '&nbsp;', '&nbsp;', '&nbsp;'],
              ['&nbsp;', '&nbsp;', '&nbsp;', '&nbsp;', '&nbsp;'],
              ['&nbsp;', '&nbsp;', '&nbsp;', '&nbsp;', '&nbsp;'],
              ['&nbsp;', '&nbsp;', '&nbsp;', '&nbsp;', '&nbsp;']],dtype=object)

def R_text(I,II,III,IV,V,VI,VII):
    R = """
                                    <td>{}</td>
                                    <td>{}</td>
                                    <td>{}</td>
                                    <td>{}</td>
                                    <td>{}</td>
                                    <td>{}</td>
                                    <td>{}</td>

    """.format(I,II,III,IV,V,VI,VII)
    return R

def generate_html(I,II,III,IV,V,name = "課表"):#time.strftime("%Y_%m_%d-%H:%M") #檔名：現在時間
    file_html = open(name+".html", "w")
    file_html.write(html1+I + html2+II + html3+III + html4+IV + html5+V)
    file_html.close()
    return print("html file done !!!")

def generate_html_array(array=O0,name = "課表"):#time.strftime("%Y_%m_%d-%H:%M") #檔名：現在時間
    file_html = open(name+".html", "w")
    O = array
    html = ""
    html += html0 + name
    html += html1 + R_text(O[0,0],O[1,0],O[2,0],O[3,0],O[4,0],O[5,0],O[6,0])
    html += html2 + R_text(O[0,1],O[1,1],O[2,1],O[3,1],O[4,1],O[5,1],O[6,1])
    html += html3 + R_text(O[0,2],O[1,2],O[2,2],O[3,2],O[4,2],O[5,2],O[6,2])
    html += html4 + R_text(O[0,3],O[1,3],O[2,3],O[3,3],O[4,3],O[5,3],O[6,3])
    html += html5 + R_text(O[0,4],O[1,4],O[2,4],O[3,4],O[4,4],O[5,4],O[6,4]) + html6
    file_html.write(html)
    file_html.close()
    return print("html file done !!!")

def WEEK(c):
    b = (c=="一")or(c=="二")or(c=="三")or(c=="四")or(c=="五")or(c=="六")or(c=="日")
    return b

def number(n):
    if n=="一":
        n = 1
    elif n=="二":
        n = 2
    elif n=="三":
        n = 3
    elif n=="四":
        n = 4
    elif n=="五":
        n = 5
    elif n=="六":
        n = 6
    elif n=="日":
        n = 7
    return n

def TIME(s):
    s = s.replace(" ", "")#去除空白
    p = []
    for i in range(len(s)):
        if WEEK(s[i]):
            p.append(i)
    for i in list(reversed(p)):
        s = s[:i] + "|" + s[i:]
    s = s[1:].split("|")
    vector = []
    for i in range(len(s)):
        element = []
        week = number(list(s[i])[0])
        time = s[0][1:]
        try:
            time = time.split(",")
        except:
            pass
        for i in range(len(time)):
            vector.append([week,time[i]])
    return vector

def find_xpath(xpath):# Xpath(列,行)
    p = driver.find_element(By.XPATH, xpath)
    return p.text

def find_column(j):
    i = 2
    C = find_xpath("//tbody/tr[1]/th[{:}]/font".format(j))
    try:
        while True:
            tex = find_xpath("//tbody/tr[{:}]/td[{:}]/font".format(i,j))
            C = np.vstack((C,tex))
            i = i+1
        else:
            pass
    except:
        pass
    return C
#--------------------------------------------------------------------------------------------------------------------------------
def REGION(s):
    n = 0
    if (s=='1')or(s=='2')or(s=='3')or(s=='A')or(s=='B'):
        n = 1
    if (s=='4')or(s=='5')or(s=='6')or(s=='C')or(s=='D'):
        n = 2
    if (s=='7')or(s=='8')or(s=='9')or(s=='E')or(s=='F'):
        n = 3
    if (s=='10')or(s=='11')or(s=='12')or(s=='G')or(s=='H'):
        n = 4
    if (s=='13')or(s=='14')or(s=='15')or(s=='I')or(s=='J'):
        n = 5
    return n
""" 0,  1,  2,    3,      4,              5,               6,   7,    8,    9,    10,     11     12,""" 
"""年級,編號,班別,科目名稱,任課教授,上課時數\n正課/實驗實習/書報討論,學分,選必,上課時間,上課地點,限修人數,課程大綱,備註""" 
def generate_array(table):
    array = np.array([['', '', '', '', ''],
                      ['', '', '', '', ''],
                      ['', '', '', '', ''],
                      ['', '', '', '', ''],
                      ['', '', '', '', ''],
                      ['', '', '', '', ''],
                      ['', '', '', '', '']],dtype=object)
    T = np.vstack((table[1:,3],table[1:,8],table[1:,4], table[1:,6], table[1:,0], table[1:,10],table[1:,9]))
    R1, R2, R3, R4, R5 = "","","","",""
    N = table.shape[0]-1
    #掃過所有的課
    for i in range(N):
        name = T[0,i] #名稱 3
        time = T[1,i] #(星期,時間) 8
        teacher = T[2,i] #任課教師 4
        num = T[3,i] #學分 6
        grade = T[4,i] #年級 0
        peo = T[5,i] #人數 10
        place = T[6,i] #地點 9
        try:
            name.replace("\n","<br>")
        except:
            pass
        s = TIME(time) #時間向量
        for j in range(len(s)): #掃過所有的上課時間
            w = list(s[j])[0]   #星期(int)
            t = list(s[j])[1]   #上課時間(str)
            r = REGION(t)       #上課區段(int)
            array[r-1,w-1] += "<div class='Class'>" + "("+t+")" + name + "<br>" + teacher
            array[r-1,w-1] += "<div class='hide'>"
            array[r-1,w-1] += "年級："+ grade + "<br>" 
            array[r-1,w-1] += "人數："+ peo + "<br>" 
            array[r-1,w-1] += "學分："+ num + "<br>"
            array[r-1,w-1] += "地點："+ place + "<br>" 
            array[r-1,w-1] += "</div></div>"
    return array



#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
#-----------------------------------------------------------------------



s = Service(r"/Users/apple/Desktop/中正大學/暑假/python 抓課表/行事曆 html/python/chromedriver")
driver = webdriver.Chrome(service=s)
driver.get("https://kiki.ccu.edu.tw/~ccmisp06/Course/index.html")
SIZE = (800,600)
driver.set_window_size(SIZE[0],SIZE[1])
driver.set_window_position(600,160)

S = True
while S == True:
    department = input("要找的科系：")
    try:
        driver.find_element(By.LINK_TEXT, department).click()
        S = False
    except:
        print("沒有符合的科系。")

try:
    #-----------------------------------------------------------------------
    table = find_column(1)
    for j in range(2,14):
        table = np.hstack((table,find_column(j)))
    SLEEP = 3 #3秒後關閉網頁
    for i in range(SLEEP):
        sleep(1)
        print(SLEEP-i)
    driver.quit()
    print("The website is closed.")
except:
    pass
print("Shape of table: ",table.shape[0],"x",table.shape[1])

array = generate_array(table)
generate_html_array(array = array,name = "{}-開課課表".format(department))












