package com.tp_ids.hoteles.hotel

import android.view.View
import android.widget.Button
import android.widget.ImageView
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView
import com.tp_ids.hoteles.R

class HotelViewHolder(view: View) : RecyclerView.ViewHolder(view) {
    private val tvHotelName: TextView = view.findViewById(R.id.tvHotelName)
    private val ivHotel: ImageView = view.findViewById(R.id.ivHotel)
    private val tvHotelDescription: TextView = view.findViewById(R.id.tvHotelDescription)
    val btnHotel: Button = view.findViewById(R.id.btnHotel)

    fun render(hotel: Hotel) {
        tvHotelName.text = hotel.name
        // TODO("poner la imagen")
        tvHotelDescription.text = hotel.description
    }
}