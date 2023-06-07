import 'dart:async';
import 'package:flutter/material.dart';
import 'package:flutter_webview_pro/webview_flutter.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter/material.dart';
import 'package:dio/dio.dart';
import 'package:path_provider/path_provider.dart';
import 'package:flutter_pdfview/flutter_pdfview.dart';
import 'package:flutter/material.dart';
import 'package:url_launcher/url_launcher.dart';
import 'package:url_launcher/url_launcher_string.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: HomeScreen(),
    );
  }
}

class AnalysisPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
          backgroundColor: Colors.cyan[400],
        title: Text('Analiz Sayfası'),
        leading: IconButton(
          icon: Icon(Icons.arrow_back),
          onPressed: () {
            // Bir önceki sayfaya geri dön
            Navigator.pop(context);
          },
        ),
      ),
      body:  Container(
        width: MediaQuery.of(context).size.width,
        height:MediaQuery.of(context).size.height ,
        padding: EdgeInsets.zero,
        child: WebView(

                  initialUrl: 'https://mertbozkurt-streamlit-analysis.hf.space',
                  javascriptMode: JavascriptMode.unrestricted,
          ),
      ),

    );
  }
}
class ScanPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.cyan[400],
        title: Text('Optik Tarayıcı'),
        leading: IconButton(
          icon: Icon(Icons.arrow_back),
          onPressed: () {
            // Bir önceki sayfaya geri dön
            Navigator.pop(context);
          },
        ),
      ),
      body:  Container(
        width: MediaQuery.of(context).size.width,
        height:MediaQuery.of(context).size.height ,
        padding: EdgeInsets.zero,
        child: WebView(

          initialUrl: 'https://mertbozkurt-omr-app.hf.space',
          javascriptMode: JavascriptMode.unrestricted,
        ),
      ),

    );
  }
}
class AnswersPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.cyan[400],
        title: Text('Cevap Anahtarı Oluştur'),
        leading: IconButton(
          icon: Icon(Icons.arrow_back),
          onPressed: () {
            // Bir önceki sayfaya geri dön
            Navigator.pop(context);
          },
        ),
      ),
      body:  Container(
        width: MediaQuery.of(context).size.width,
        height:MediaQuery.of(context).size.height ,
        padding: EdgeInsets.zero,
        child: WebView(

          initialUrl: 'https://mertbozkurt-answers.hf.space',
          javascriptMode: JavascriptMode.unrestricted,
        ),
      ),

    );
  }
}
class PdfPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.cyan[400],
        title: Text('Optikler'),
        leading: IconButton(
          icon: Icon(Icons.arrow_back),
          onPressed: () {
            // Bir önceki sayfaya geri dön
            Navigator.pop(context);
          },
        ),
      ),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [Text("Optik 1",
        style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),),
          Text("3 farklı ders ve her bir ders için 20 soru bulunmakta."),
          Text("10 haneli öğrenci numarası işaretlenebilmektedir."),
          Container(
            margin: EdgeInsets.all(12.0),
            child: Image.network(
              'https://i.ibb.co/DLNdd4c/image-2023-06-07-163956424.png',
              fit: BoxFit.cover,
            ),
          ),
          SizedBox(height: 10.0),

          ElevatedButton.icon(
            onPressed: () {
              _launchURL();
            },
            icon: const Icon(Icons.download_for_offline),
            style: ElevatedButton.styleFrom(
                backgroundColor: Colors.lightGreenAccent,
                shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(50)),

                padding:
                const EdgeInsets.symmetric(horizontal: 10, vertical: 10),
                textStyle:
                const TextStyle(fontSize: 20, fontWeight: FontWeight.bold)),
            label: const Text('PDF i indirmek için tıklayın',
                style: TextStyle(color: Colors.black54)),
          ),
          SizedBox(height: 16.0),
        ],
      ),
    );
  }

  _launchURL() async {
    final Uri url = Uri.parse('https://drive.google.com/file/d/1_A1q5O0ZztctYUPUFxEwBuJpX7y-O_yd/view?usp=sharing');
    if (!await launchUrl(url,mode: LaunchMode.externalApplication)) {
      throw Exception('Link Açılamadı');
    }
  }
}

class UserGuidePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.cyan[400],
        title: Text('Kullanım Kılavuzu'),
        leading: IconButton(
          icon: Icon(Icons.arrow_back),
          onPressed: () {
            // Bir önceki sayfaya geri dön
            Navigator.pop(context);
          },
        ),
      ),
      body: SingleChildScrollView(
        padding: EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(
              'Adım 1:',
              style: TextStyle(
                fontSize: 18.0,
                fontWeight: FontWeight.bold,
              ),
            ),
            Text('Öncelikle bir öğretmen koduna ve bir şifreye ihtiyaç duyacaksınız. Bunu iletişim kısmından bizlerden talep ileterek edinebilirsiniz.'),
            SizedBox(height: 8.0),
            Text(
              'Adım 2: Cevap Anahtarı Oluşturma',
              style: TextStyle(
                fontSize: 18.0,
                fontWeight: FontWeight.bold,
              ),
            ),
            Text("Bu adımda yaptığınız sınavın cevap anahtarını oluşturmanız gerekmektedir. Bunun için Cevap Kağıdı Oluştur butonuna tıklayarak ilgili sayfaya gidebilirsiniz. Cevap anahtarı oluşturmak için elinizde bulunan bir optiğe doğru şıkları işaretlemeniz ve sonrasında sayfa üzerinde taramanız gerekir. Tarama işleminin ardından sizlere tanımlanmış 5 adet cevap anahtarı kayıt alanında birini seçiniz. İşlemleri yaptıktan sonra ekranda görünen şıkları kontrol edip kayıt işlemini sonlandırabilirsiniz."),
            SizedBox(height: 8.0),
            // Diğer adımların listesi burada yer alır...

            SizedBox(height: 16.0),
            Image.asset(
              'assets/images/user_guide_image.jpg',
              fit: BoxFit.cover,
            ),
          ],
        ),
      ),
    );
  }
}

class HomeScreen extends StatefulWidget {
  @override
  _HomeScreenState createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  @override
  Widget build(BuildContext context) {
    // to get size
    var size = MediaQuery.of(context).size;

    // style
    var cardTextStyle = TextStyle(
        fontFamily: "Montserrat Regular",
        fontSize: 14,
        color: Color.fromRGBO(63, 63, 63, 1));

    return Scaffold(

      body: Stack(
        children: <Widget>[
          Container(
            height: size.height * .3,
            decoration: BoxDecoration(
              image: DecorationImage(
                  alignment: Alignment.topCenter,
                  image: AssetImage('assets/images/top_header.png')),
            ),
          ),
          SafeArea(
            child: Padding(
              padding: EdgeInsets.all(16.0),
              child: Column(
                children: <Widget>[
                  Container(
                    height: 64,
                    margin: EdgeInsets.only(bottom: 20,top: 20),
                    child: Text(
                      'Optik Okuyucu',
                      style: TextStyle(
                          fontFamily: "Montserrat Medium",
                          color: Colors.white,
                          fontSize: 35),
                    ),
                  ),
                  Expanded(
                    child: GridView.count(
                      mainAxisSpacing: 10,
                      crossAxisSpacing: 10,
                      primary: false,
                      crossAxisCount: 2,
                      children: <Widget>[
                        Card(
                          shape:RoundedRectangleBorder(
                              borderRadius: BorderRadius.circular(8)
                          ),
                          elevation: 4,
                          child: InkWell(
                            onTap: () {
                              Navigator.push(
                              context,
                              MaterialPageRoute(builder: (context) => ScanPage()),
                            );
                            },
                            child: Column(
                              mainAxisAlignment: MainAxisAlignment.center,
                              children: <Widget>[
                                Image.network(
                                  'https://cdn-icons-png.flaticon.com/512/1922/1922725.png',
                                  height: 128,
                                ),
                                Text(
                                  'Tarayıcı Sayfası',
                                  style: cardTextStyle,
                                )
                              ],
                            ),
                          ),
                        ),

                        Card(
                          shape:RoundedRectangleBorder(
                              borderRadius: BorderRadius.circular(8)
                          ),
                          elevation: 4,
                          child: InkWell(
                            onTap: () {
                              Navigator.push(
                                context,
                                MaterialPageRoute(builder: (context) => AnswersPage()),
                              );
                            },
                            child: Column(
                              mainAxisAlignment: MainAxisAlignment.center,
                              children: <Widget>[
                                Image.network(
                                  'https://cdn-icons-png.flaticon.com/512/5732/5732163.png',
                                  height: 128,
                                ),
                                Text(
                                  'Cevap Kağıdı Oluştur',
                                  style: cardTextStyle,
                                )
                              ],
                            ),
                          ),
                        ),

                        Card(
                          shape:RoundedRectangleBorder(
                              borderRadius: BorderRadius.circular(8)
                          ),
                          elevation: 4,
                          child: InkWell(
                               onTap: () {
                                Navigator.push(
                                  context,
                                  MaterialPageRoute(builder: (context) => AnalysisPage()),
                                );
                              },
                            child: Column(
                              mainAxisAlignment: MainAxisAlignment.center,
                              children: <Widget>[
                                Image.network(
                                  'https://cdn-icons-png.flaticon.com/512/2235/2235667.png',
                                  height: 128,
                                ),
                                Text(
                                  'Analiz Sayfası',
                                  style: cardTextStyle,
                                )
                              ],
                            ),
                          ),
                        ),

                        Card(
                          shape:RoundedRectangleBorder(
                              borderRadius: BorderRadius.circular(8)
                          ),
                          elevation: 4,
                          child: InkWell(
                            onTap: () {
                              Navigator.push(
                                context,
                                MaterialPageRoute(builder: (context) => PdfPage()),
                              );
                            },
                            child: Column(
                              mainAxisAlignment: MainAxisAlignment.center,
                              children: <Widget>[
                                Image.network(
                                  'https://www.iconpacks.net/icons/2/free-pdf-download-icon-2617-thumb.png',
                                  height: 128,
                                ),
                                Text(
                                  'Optikler',
                                  style: cardTextStyle,
                                )
                              ],
                            ),
                          ),
                        ),

                        Card(
                          shape:RoundedRectangleBorder(
                              borderRadius: BorderRadius.circular(8)
                          ),
                          elevation: 4,
                          child: InkWell(
                            onTap: () {
                              Navigator.push(
                                context,
                                MaterialPageRoute(builder: (context) => UserGuidePage()),
                              );
                            },
                            child: Column(
                              mainAxisAlignment: MainAxisAlignment.center,
                              children: <Widget>[
                                Image.network(
                                  'https://cdn-icons-png.flaticon.com/512/167/167534.png',
                                  height: 128,
                                ),
                                Text(
                                  'Kullanım',
                                  style: cardTextStyle,
                                )
                              ],
                            ),
                          ),
                        ),

                        Card(
                          shape:RoundedRectangleBorder(
                              borderRadius: BorderRadius.circular(8)
                          ),
                          elevation: 4,
                          child: InkWell(
                            onTap: () {
                              Navigator.push(
                                context,
                                MaterialPageRoute(builder: (context) => ScanPage()),
                              );
                            },

                            child: Column(
                              mainAxisAlignment: MainAxisAlignment.center,
                              children: <Widget>[
                                Image.network(
                                  'https://static.vecteezy.com/system/resources/previews/010/153/863/original/email-and-mail-icon-sign-symbol-design-free-png.png',
                                  height: 128,
                                ),
                                Text(
                                  'İletişim',
                                  style: cardTextStyle,
                                )
                              ],
                            ),
                          ),
                        ),
                      ],
                    ),
                  ),
                ],
              ),
            ),
          ),
        ],
      ),
    );
  }
}
