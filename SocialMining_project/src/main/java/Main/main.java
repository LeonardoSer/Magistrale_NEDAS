package Main;

import lucene.Indexer;
import org.apache.lucene.document.Document;
import org.apache.lucene.index.DirectoryReader;
import org.apache.lucene.index.IndexReader;
import org.apache.lucene.index.Term;
import org.apache.lucene.search.*;
import org.apache.lucene.store.Directory;
import org.apache.lucene.store.SimpleFSDirectory;
import org.json.JSONArray;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.file.FileSystems;
import java.util.ArrayList;
import java.util.zip.GZIPInputStream;

public class main {
    public static void main(String[] args) throws IOException {

/*
        String dataSet_path = "/home/leonardo/IdeaProjects/socialMining/src/main/java/Main/dataset.gz";
        DatasetIndexer.indexDataSet(dataSet_path);
*/

        ArrayList<ArrayList<Document>> windows_byDay = WindowGeneratorByDay.getSlidingWindows(10, 5);
        ArrayList<ArrayList<Document>> windows_byHour = WindowGeneratorByHours.getSlidingWindows(5, 60);

        int i = 0;
        for (ArrayList<Document> window:windows_byDay) {
            System.out.println("window " + i + ", size -> " + window.size());
            i++;
        }

        System.out.println("\n Ti piace il cazzo, lo vuoi il mio Stilo?\n ");

        i = 0;
        for (ArrayList<Document> window:windows_byHour) {
            System.out.println("window " + i + ", size -> " + window.size());
            i++;
        }

        windows_byDay.get(0).get(0).getField("text").tokenStream();

    }
}
