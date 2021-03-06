package com.shreybatra.builduppharma;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import com.android.volley.DefaultRetryPolicy;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.Volley;
import com.google.gson.JsonArray;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {

    Button b1;
    public static final String TAG = "PT";
    public static final String URL = "https://9701aada.ngrok.io/medicine";

    EditText m1,m2,m3,m4,m5,q1,q2,q3,q4,q5,lt,lg;

    TextView t1;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        b1 = (Button) findViewById(R.id.submit);

        t1 = (TextView) findViewById(R.id.t1);

        m1 = (EditText) findViewById(R.id.medicine_name0);
        m2 = (EditText) findViewById(R.id.medicine_name1);
        m3 = (EditText) findViewById(R.id.medicine_name2);
        m4 = (EditText) findViewById(R.id.medicine_name3);
        m5 = (EditText) findViewById(R.id.medicine_name4);

        q1 = (EditText) findViewById(R.id.medicine_qty0);
        q2 = (EditText) findViewById(R.id.medicine_qty1);
        q3 = (EditText) findViewById(R.id.medicine_qty2);
        q4 = (EditText) findViewById(R.id.medicine_qty3);
        q5 = (EditText) findViewById(R.id.medicine_qty4);


        lt = (EditText) findViewById(R.id.lat);
        lg = (EditText) findViewById(R.id.lng);

        b1.setOnClickListener(new View.OnClickListener() {

            public void onClick(View view) {

                ArrayList<String> medicines = new ArrayList<String>();

                ArrayList <String> quantities= new ArrayList<String>();



                medicines.add(m1.getText().toString());
                medicines.add(m2.getText().toString());
                medicines.add(m3.getText().toString());
                medicines.add(m4.getText().toString());
                medicines.add(m5.getText().toString());

                quantities.add(q1.getText().toString());
                quantities.add(q2.getText().toString());
                quantities.add(q3.getText().toString());
                quantities.add(q4.getText().toString());
                quantities.add(q5.getText().toString());

                JSONObject request = new JSONObject();

                try {
                    request.put("medicines",new JSONArray(medicines));
                    request.put("quantities",new JSONArray(quantities));
                    request.put("lat",lt.getText().toString());
                    request.put("lng",lg.getText().toString());
                } catch (JSONException e) {
                    e.printStackTrace();
                }

                func(request);
            }
        });


    }

    public void func( JSONObject jsonObject)
    {
        RequestQueue queue= Volley.newRequestQueue(this);

        //JSONObject jsonObject = new JSONObject();

        //t1.setText(jsonObject.toString());

        JsonObjectRequest request = new JsonObjectRequest(Request.Method.POST,URL, jsonObject, new Response.Listener<JSONObject>() {
            @Override
            public void onResponse(JSONObject response) {
                //Log.d(TAG, "onResponse: " + response.toString());

                try {
                    disp(response);
                } catch (JSONException e) {
                    e.printStackTrace();
                }


            }
        }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {
                Log.d(TAG, "onErrorResponse: "+error.toString());
            }
        });

        request.setRetryPolicy(new DefaultRetryPolicy(100000,
                DefaultRetryPolicy.DEFAULT_MAX_RETRIES,
                DefaultRetryPolicy.DEFAULT_BACKOFF_MULT));

        queue.add(request);
    }

    public void disp(JSONObject jsonObject) throws JSONException {

        JSONArray arr = jsonObject.getJSONArray("Result");

        String s = "";

        for(int i=0;i<arr.length();i++)
        {
            JSONObject j = (JSONObject) arr.get(i);
            s += j.getString("name") + "\n";
            s += "Count of Medicines - " + new Integer(j.getInt("count")).toString() + "\n\n";

        }

        t1.setText(s.toString());

    }
}
