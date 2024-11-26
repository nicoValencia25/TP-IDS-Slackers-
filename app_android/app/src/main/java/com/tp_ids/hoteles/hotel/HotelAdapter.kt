package com.tp_ids.hoteles.hotel

import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import com.tp_ids.hoteles.R

class HotelAdapter(private val hotels: List<Hotel>, private val onTaskSelected: (Int) -> Unit) : RecyclerView.Adapter<HotelViewHolder>() {
    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): HotelViewHolder {
        val view =
            LayoutInflater.from(parent.context).inflate(R.layout.item_hotel, parent, false)
        return HotelViewHolder(view)
    }

    override fun getItemCount() = hotels.size

    override fun onBindViewHolder(holder: HotelViewHolder, position: Int) {
        holder.render(hotels[position])
        holder.btnHotel.setOnClickListener { onTaskSelected(hotels[position].id) }
    }
}