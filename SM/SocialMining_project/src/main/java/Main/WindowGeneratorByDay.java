package Main;

import org.apache.lucene.analysis.Analyzer;
import org.apache.lucene.analysis.standard.StandardAnalyzer;
import org.apache.lucene.document.Document;
import org.apache.lucene.index.DirectoryReader;
import org.apache.lucene.index.IndexReader;
import org.apache.lucene.index.Term;
import org.apache.lucene.queryparser.classic.QueryParser;
import org.apache.lucene.search.*;
import org.apache.lucene.store.Directory;
import org.apache.lucene.store.SimpleFSDirectory;

import java.io.IOException;
import java.nio.file.FileSystems;
import java.util.ArrayList;
import java.util.List;

public class WindowGeneratorByDay {

    // retrieve a document by month and day then it appends it to the 'result' array (so it appends a day of tweets to the window)
    private static ArrayList<Document> windowAppender(String month, String day, ArrayList<Document> result) throws IOException{

        if(day.length() == 1){
            day = "0" + day;
        }



        IndexReader ir;
        Directory dir = new SimpleFSDirectory(FileSystems.getDefault().getPath("tweets_index"));
        ir = DirectoryReader.open(dir);

        IndexSearcher searcher = new IndexSearcher(ir);

        PhraseQuery.Builder builder = new PhraseQuery.Builder();
        builder.add(new Term("created_at", month), 1);
        builder.add(new Term("created_at", day), 2);
        PhraseQuery q = builder.build();


        TopDocs top = searcher.search(q, ir.numDocs());
        ScoreDoc[] hits = top.scoreDocs; // scoreDocs è una tupla es. {doc=1 score=0.3150669 shardIndex=0}

        Document doc = null;
        for (ScoreDoc entry : hits) {
            //carichiamo in memoria il documento, solo i file memorizzati sono disponibili
            doc = searcher.doc(entry.doc); // stesso di `ir.document(entry.doc);`
            result.add(doc);
        }

        return result;
    }

    // create an array made up of tweets from "day" to "day+len" (creates a window of len days)
    public static ArrayList<Document> getWindow(String month, String day, int len) throws IOException {

        ArrayList<Document> window = new ArrayList<Document>();

        int j = 0;
        for(int i=0; i<len; i++){

            window = windowAppender(month, Integer.toString(Integer.parseInt(day) + j), window);

            if(Integer.parseInt(day) + j == 31){
                day = "1";
                month = "feb";
                j = 0;


            }else{
                j++;
            }
        }
        return window;
    }

    // creates all windows of lenght 'len' from the whole dataset with a given slide
    public static ArrayList<ArrayList<Document>> getSlidingWindows(int len, int slide) throws IOException{

        ArrayList<ArrayList<Document>> allWindows = new ArrayList<ArrayList<Document>>();

        int day = 1;
        String month = "jan";

        while(!(day>28 && month.equals("feb"))){

            ArrayList<Document> curr_window = getWindow(month, Integer.toString(day), len);
            allWindows.add(curr_window);


            day += slide;
            if(day > 31){
                day = -1 * (31 - day);
                month = "feb";
            }
        }

        return allWindows;
    }
}
