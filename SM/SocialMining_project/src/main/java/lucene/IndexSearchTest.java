package lucene;

import org.apache.lucene.document.Document;
import org.apache.lucene.index.DirectoryReader;
import org.apache.lucene.index.IndexReader;
import org.apache.lucene.index.Term;
import org.apache.lucene.search.*;
import org.apache.lucene.store.Directory;
import org.apache.lucene.store.SimpleFSDirectory;

import java.nio.file.FileSystems;

public class IndexSearchTest {

    public static void main(String[] args) throws Throwable {
        Directory dir = new SimpleFSDirectory(FileSystems.getDefault().getPath("idcard-index")); // dobbiamo usare la stessa directory definita per l'Indexer
        IndexReader ir = DirectoryReader.open(dir);

        IndexSearcher searcher = new IndexSearcher(ir);

        // es.1
        Query q = new TermQuery(new Term("name", "doradaccelancora")); // il nome va cercato tutto in minuscolo perchè l'IDcard è stata tokenizzata

        // es.2
        // Query q = LongPoint.newRangeQuery("bdate", 0L, 26121998+1L);

        // es.3 -> chepperò non funziona
        // Analyzer anal = new ItalianAnalyzer(); //new StandardAnalyzer() va bene comunque
        // QueryParser parser = new QueryParser("name", anal);
        // Query q = parser.parse("bio:culo");

        TopDocs top = searcher.search(q, 100); // prenede i primi 100 risultati della query
        ScoreDoc[] hits = top.scoreDocs; // scoreDocs è una tupla es. {doc=1 score=0.3150669 shardIndex=0}
        Document doc = null;

        for(ScoreDoc entry: hits){
            //carichiamo in memoria il documento, solo i file memorizzati sono disponibili
            doc = searcher.doc(entry.doc); // stesso di `ir.document(entry.doc);`

            System.out.println("Score: " + entry);
            System.out.println("Tag: " + doc.get("tag"));
            System.out.println("Name: " + doc.get("name"));
            System.out.println("Bdate: " + doc.get("bdate"));
            System.out.println("Bio: " + doc.get("bio"));
            System.out.println("height: " + doc.get("height"));

        }
    }
}
