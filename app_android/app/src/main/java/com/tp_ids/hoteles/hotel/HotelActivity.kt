package com.tp_ids.hoteles.hotel

import android.os.Bundle
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.tp_ids.hoteles.R

class HotelActivity : AppCompatActivity() {
    private lateinit var hotels: MutableList<Hotel>

    private lateinit var rvHotel: RecyclerView
    private lateinit var hotelAdapter: HotelAdapter

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContentView(R.layout.activity_hotel)
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main)) { v, insets ->
            val systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars())
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom)
            insets
        }

        initComponent()
        initUI()
    }

    private fun initComponent() {
        // TODO hotels desde la api
        hotels = mutableListOf(
            Hotel(
                1,
                "Hotel 1",
                "http://www.cfmedia.vfmleonardo.com/imageRepo/6/0/100/3/616/bkksi-exterior-0385-hor-clsc_O.jpg",
                "Es el primer hotel"
            ),
            Hotel(
                2,
                "Hotel 2",
                "https://i.pinimg.com/originals/3d/65/98/3d6598f418272467bfe4d184adeb399d.jpg",
                "Es el segundo hotel"
            ),
            Hotel(
                3,
                "Hotel 3",
                "https://media.cntraveler.com/photos/5841fe31e186e2555afdd5ca/master/pass/alfond-inn-cr-courtesy.jpg",
                "Es el tercer hotel"
            )
        )

        rvHotel = findViewById(R.id.rvHotel)
    }

    private fun initUI() {
        hotelAdapter = HotelAdapter(hotels)
        rvHotel.layoutManager = LinearLayoutManager(this)
        rvHotel.adapter = hotelAdapter
    }
}