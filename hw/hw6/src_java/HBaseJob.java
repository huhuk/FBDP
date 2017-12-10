import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.hbase.*;
import org.apache.hadoop.hbase.client.*;
import org.apache.hadoop.hbase.util.Bytes;

import java.io.*;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;

public class HBaseJob {

    public static void main(String[] args) throws IOException {
        System.out.println("init...");
        Configuration cfg = HBaseConfiguration.create();
        cfg.set("hbase.zookeeper.quorum", "localhost");
//        cfg.set("hbase.zookeeper.property.clientPort", "2181");
        Connection conn = ConnectionFactory.createConnection(cfg);

        String tableName = null;
        HashSet<String> cfs = new HashSet<>();
        HashMap<String, String> q_cf = new HashMap<>();
        System.out.println("\n");

//      read meta
        System.out.println("read meta...");
        String filename = "/home/huhu/pyenv/java_stu.table";
        File file = new File(filename);
        BufferedReader reader = null;
        try {
            System.out.println("read line: \n");
            reader = new BufferedReader(new FileReader(file));
            String tmp;
            tableName = reader.readLine();
            while ( (tmp = reader.readLine()) != null ) {
                String[] t1 = tmp.split(":", 2);
                cfs.add(t1[0]);
                for (String val: t1[1].split(",")
                     ) {
                    q_cf.put(val, t1[0]);
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            try {
                reader.close();
            } catch (IOException e1) {
            }
        }
        System.out.println("\n");

//        create table
        Admin admin = conn.getAdmin();
        HTableDescriptor t = new HTableDescriptor(TableName.valueOf(tableName));
        for (String cf: cfs
             ) {
            t.addFamily(new HColumnDescriptor(cf));
        }
        if (admin.tableExists(TableName.valueOf(tableName))) {
            System.out.println("exists!\n");
            admin.disableTable(TableName.valueOf(tableName));
            admin.deleteTable(TableName.valueOf(tableName));
        }
        admin.createTable(t);

        Table table = conn.getTable(TableName.valueOf(tableName));
        List<Put> puts = new LinkedList<>();
//      read data
        System.out.println("read data...");
        String fileData = "/home/huhu/pyenv/students.data";
        file = new File(fileData);
        System.out.println("read data: \n");
        reader = new BufferedReader(new FileReader(file));
        String line = null;
        while( (line = reader.readLine()) != null ) {
            String[] t1 = line.split(" ", 2);
            Put put = new Put(Bytes.toBytes(t1[0]));
            for (String q_val: t1[1].split(",")
                 ) {
                String q = q_val.split(":")[0];
                String val = q_val.split(":")[1];
                String f = q_cf.get(q);
                put.addColumn(Bytes.toBytes(f), Bytes.toBytes(q), Bytes.toBytes(val));
                puts.add(put);
            }
        }
        table.put(puts);
        System.out.println("\n");

//      scan table
        System.out.println("scan table: " + tableName + "\n");
        ResultScanner ss = table.getScanner(new Scan());
        for (Result r: ss
                ) {
            for (Cell cell : r.listCells()
                 ) {
                String row = new String(CellUtil.cloneRow(cell));
                String family = new String(CellUtil.cloneFamily(cell));
                String column = new String(CellUtil.cloneQualifier(cell));
                String value = new String(CellUtil.cloneValue(cell));
                long timestamp = cell.getTimestamp();
                System.out.printf("%-20s column=%s:%s, timestamp=%s, value=%s\n",
                        row, family, column, timestamp, value);
            }
        }
    }
}
