package lucene;

import org.apache.lucene.analysis.Analyzer;
import org.apache.lucene.analysis.standard.StandardAnalyzer;
import org.apache.lucene.index.IndexWriter;
import org.apache.lucene.index.IndexWriterConfig;
import org.apache.lucene.store.Directory;
import org.apache.lucene.store.SimpleFSDirectory;

import java.nio.file.FileSystems;

public class Indexer {

    public void indexing(IDcard [] cards) throws Throwable{

        Directory dir = new SimpleFSDirectory(FileSystems.getDefault().getPath("idcard-index")); // directory persistente
        // Directory dir = new ByteBuffersDirectory(); // directory volatile

        Analyzer anal = new StandardAnalyzer();
        IndexWriterConfig cfg = new IndexWriterConfig(anal);
        IndexWriter writer = new IndexWriter(dir, cfg);

        for(IDcard card: cards){
           System.out.println("indexing card_ " + card.Tag);
           card.updateDoc();
           writer.addDocument(IDcard.doc);
        }

        writer.commit();
        writer.close();
        dir.close();



    }

}
