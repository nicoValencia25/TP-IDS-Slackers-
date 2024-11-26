package com.tp_ids.hoteles.room

import android.os.Bundle
import android.util.Log
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.tp_ids.hoteles.R

class RoomActivity : AppCompatActivity() {
    var hotelID: Int = 1
    private lateinit var rooms: MutableList<Room>

    private lateinit var rvRoom: RecyclerView
    private lateinit var roomAdapter: RoomAdapter

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContentView(R.layout.activity_room)
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main)) { v, insets ->
            val systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars())
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom)
            insets
        }

        hotelID = intent.extras?.getInt("hotelID") ?: 1
        initComponent()
        initUI()
    }

    private fun initComponent() {
        rooms = mutableListOf(
            Room(
                1,
                "Habitación 1",
                "http://www.cfmedia.vfmleonardo.com/imageRepo/6/0/100/3/616/bkksi-exterior-0385-hor-clsc_O.jpg",
                "La primer habitación",
                4,
                10000,
                2000000,
                // Hotel
                1,
                101
            ),
            Room(
                2,
                "Habitación 2",
                "http://www.cfmedia.vfmleonardo.com/imageRepo/6/0/100/3/616/bkksi-exterior-0385-hor-clsc_O.jpg",
                "La segunda habitación",
                6,
                10000,
                2000000,
                // Hotel
                1,
                102
            ),
            Room(
                3,
                "Habitación 3",
                "http://www.cfmedia.vfmleonardo.com/imageRepo/6/0/100/3/616/bkksi-exterior-0385-hor-clsc_O.jpg",
                "La tercer habitación",
                2,
                10000,
                2000000,
                // Hotel
                2,
                201
            )
        )

        rvRoom = findViewById(R.id.rvRoom)
    }

    private fun initUI() {
        roomAdapter = RoomAdapter(rooms)
        rvRoom.layoutManager = LinearLayoutManager(this)
        rvRoom.adapter = roomAdapter
    }
}