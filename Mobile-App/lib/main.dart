import 'dart:async';
import 'package:flutter/material.dart';
import 'package:flutter_webview_pro/webview_flutter.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: MainPage(),
    );
  }
}
class HomePage extends StatelessWidget {

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text("Scan Page"),
          leading: IconButton(
            icon: Icon(Icons.arrow_back),
            onPressed: () {
              // Bir önceki sayfaya geri dön
              Navigator.pop(context);
            },
          ),
        ),
        body: WebView(

          initialUrl: 'https://mertbozkurt-omr-app.hf.space',
          javascriptMode: JavascriptMode.unrestricted,

        ),
      ),
    );
  }
}

class SecondPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Analysis Page'),
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

class MainPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: Text('Second Page'),
        ),
        body: GridView.builder(
          gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
            crossAxisCount: 2,
            mainAxisSpacing: 8,
            crossAxisSpacing: 8,
          ),
          itemCount: 6,
          itemBuilder: (context, index) {
            return Container(
              padding: EdgeInsets.all(8),
              child: ElevatedButton(
                onPressed: () {
                  if (index == 0) {
                    Navigator.push(
                      context,
                      MaterialPageRoute(builder: (context) => HomePage()),
                    );
                  } else if (index == 1) {
                    Navigator.push(
                      context,
                      MaterialPageRoute(builder: (context) => SecondPage()),
                    );
                  } else {
                    print('Button $index was pressed');
                  }
                },
                child: Icon(
                  // Butona atanan ikon
                  index == 0 ? Icons.document_scanner :
                  index == 1 ? Icons.grading :
                  index == 2 ? Icons.folder :
                  index == 3 ? Icons.shopping_cart :
                  index == 4 ? Icons.settings :
                  Icons.person,
                  size: 32,
                ),
              ),
            );
          },
        )
    );
  }
}


class CsvPage extends StatelessWidget {

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text("Csv Page"),
          leading: IconButton(
            icon: Icon(Icons.arrow_back),
            onPressed: () {
              // Bir önceki sayfaya geri dön
              Navigator.pop(context);
            },
          ),
        ),
        body:

    );
  }
}