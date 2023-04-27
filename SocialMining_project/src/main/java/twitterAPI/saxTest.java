package twitterAPI;


import net.seninp.jmotif.sax.SAXException;
import net.seninp.jmotif.sax.SAXProcessor;
import net.seninp.jmotif.sax.alphabet.NormalAlphabet;
import net.seninp.jmotif.sax.datastructure.SAXRecords;

// creiamo una rappresentazione per una data timeserie
public class saxTest {
    public static void main(String[] args) throws SAXException {
        // nell'output la time series è rappresentata come una seguenza di 'a' e 'b'
         // dove un simbolo viene associato ai bassi valori e uno agli alti valori
          // più è grande l'alfabeto più lo è la precisione nella rappresentazione
           // se usare pochi o tanto simboli dipende dall'obbiettivo che vogliamo raggiungere
        int alphabetSize = 2;
        double nThreshold = 0.01;

        NormalAlphabet na = new NormalAlphabet(); // Gaussian distribution for the alphabet
        SAXProcessor sp = new SAXProcessor();

        //data
        double[] ts = {10, 20, 20, 50, 80, 10, 50, 80, 10, 5};

        // discretizazzione
        SAXRecords res = sp.ts2saxByChunking(ts, ts.length, na.getCuts(alphabetSize), nThreshold);

        //print output
        String sax = res.getSAXString("");
        System.out.println(sax);
        System.out.println(sax.matches("a+b+a*b*a*")); // posso applicare REGEX alle sax strings

    }
}
