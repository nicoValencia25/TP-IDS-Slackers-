package com.tp_ids.hoteles.room

import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import com.tp_ids.hoteles.R

class RoomAdapter(private val rooms: List<Room>) :RecyclerView.Adapter<RoomViewHolder>() {
    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): RoomViewHolder {
        val view =
            LayoutInflater.from(parent.context).inflate(R.layout.item_room, parent, false)
        return RoomViewHolder(view)
    }

    override fun getItemCount() = rooms.size

    override fun onBindViewHolder(holder: RoomViewHolder, position: Int) {
        holder.render(rooms[position])
    }
}